from __future__ import annotations

import re

from abc import abstractmethod
from typing import Callable, List, Optional

class Node:

    def __init__(self, name: str, parent: Folder) -> None:
        self._name = name
        self._parent = parent

    def name(self) -> str:
        return self._name

    def parent(self) -> Folder:
        return self._parent

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def pretty_str(self, indent: int):
        pass
    
    def __str__(self) -> str:
        return self.name()

    @abstractmethod
    def is_folder(self) -> bool:
        pass


class File(Node):

    def __init__(self, name: str, parent: Folder, size: int) -> None:
        super().__init__(name, parent)
        self._size = size
        self._parent.add_child(self)

    def size(self) -> int:
        return self._size

    def pretty_str(self, indent: int = 0):
        print(f'{" " * indent}{self.name()}')

    def is_folder(self) -> bool:
        return False


class Folder(Node):

    def __init__(self, name: str, parent: Optional[Folder]=None) -> None:
        self._children = {}
        self._parent = self if parent is None else parent
        super().__init__(name, self._parent)
        if parent is not None:
            self._parent.add_child(self)

    def add_child(self, child: Node):
        self._children[child.name()] = child

    def get_child(self, name: str) -> Node:
        return self._children[name]
    
    def get_children(self) -> List[Node]:
        return list(self._children.values())

    def size(self) -> int:
        # Not worth caching with our test data input size
        return sum([self._children[child].size() for child in self._children])

    def pretty_str(self, indent: int = 0):
        print(f'{" " * indent}{self.name()}')
        for child in self._children:
            self._children[child].pretty_str(indent + 2)

    def is_folder(self) -> bool:
        return True


INPUT = 'day7-input.txt'
ROOT = Folder("/")

FILESYSTEM_SIZE = 70000000
REQUIRED_SPACE = 30000000

COMMAND_REGEX = re.compile(r'^\$\s+(?P<command>cd|ls)(\s+(?P<destination>\S+))?$')
LS_REGEX = re.compile(r'^(?P<size>\S+)\s+(?P<name>\S+)$')


def parse_file_structure(lines: List[str], root: Folder):
    current_folder = root
    i = 0
    while i < len(lines):
        match = COMMAND_REGEX.match(lines[i])
        if not match:
            raise Exception(f'Expected line to match "^\$\s+(cd\s+(\S+)|ls)$", found: {lines[i]}')
        
        command = match.group('command')
        if command == 'cd':
            dest = match.group('destination')
            if dest == '..':
                current_folder = current_folder.parent()
            elif dest == '/':
                current_folder = root
            else:
                current_folder = current_folder.get_child(dest)
            i += 1
        elif command == 'ls':
            i += 1
            while i < len(lines) and not lines[i].startswith('$'):
                match = LS_REGEX.match(lines[i])
                if not match:
                    raise Exception(f'Expected line to match "^\S+\s+\S+$", found: {lines[i]}')
                elif match.group('size') == 'dir':
                    Folder(match.group('name'), current_folder)
                else:
                    File(match.group('name'), current_folder, int(match.group('size')))
                i += 1
        else:
            raise Exception(f'Excepted "cd" or "ls", found: {command}')


def find_folders(root: Folder, condition: Callable[[Folder], bool]):
    found = []
    if condition(root):
        found = [root]
    for child in root.get_children():
        if child.is_folder():
            found.extend(find_folders(child, condition))
    return found


if __name__ == "__main__":
    with open(INPUT, 'r') as f:
        lines = f.readlines()

    parse_file_structure(lines, ROOT)

    # Part 1 - Sum the size of all folders smaller than 100_000
    folders = find_folders(ROOT, lambda x: x.size() <= 100000)
    total_size = sum([f.size() for f in folders])
    print(f'Part 1: {total_size}')

    # Part 2 - Find the size of the smallest folder that can be deleted to free up REQUIRED_SPACE 
    root_size = ROOT.size()
    must_delete = REQUIRED_SPACE - (FILESYSTEM_SIZE - ROOT.size())
    folders = find_folders(ROOT, lambda x: x.size() >= must_delete)
    smallest_size = min([f.size() for f in folders])
    print(f'Part 2: {smallest_size}')