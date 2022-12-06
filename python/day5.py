import re

from copy import deepcopy
from typing import List


INPUT = 'day5-input.txt'
MOVE_REGEX = re.compile(r'^move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)$')


class Move:
    def __init__(self, move: str) -> None:
        parsed_move = MOVE_REGEX.match(move)
        self._count = int(parsed_move.group('count'))
        self._from = int(parsed_move.group('from')) - 1
        self._to = int(parsed_move.group('to')) - 1

    def apply_9000(self, stacks: List[List[str]]) -> None:
        # Move items one at a time
        for _ in range(self._count):
            stacks[self._to].append(stacks[self._from].pop())

    def apply_9001(self, stacks: List[List[str]]) -> None:
        # Move items in one chunk
        stacks[self._to].extend(stacks[self._from][-self._count:])
        stacks[self._from] = stacks[self._from][:-self._count]


def create_stacks(lines: List[str]) -> List[List[str]]:
    stacks = [[] for _ in range(len(lines[0]) // 4)]
    for i in range(len(lines)-1):
        line = lines[i]
        for j in range(0, len(line), 4):
            item = line[j+1]
            if item != ' ':
                stacks[j//4].append(item)
    for stack in stacks:
        stack.reverse()
    return stacks


def create_moves(lines: List[str]) -> List[Move]:
    return [Move(line) for line in lines]


def create_word(stacks: List[List[str]]) -> str:
    # Join together the last letter in each stack
    return ''.join([stack[-1] for stack in dupe_stacks])


if __name__ == '__main__':

    # Parse input
    with open(INPUT, 'r') as f:
        lines = f.readlines()
    split_index = lines.index('\n')
    stacks = create_stacks(lines[:split_index])
    moves = create_moves(lines[split_index+1:])
    
    # Part 1 - Apply each move, move items one at a time
    dupe_stacks = deepcopy(stacks)
    for move in moves:
        move.apply_9000(dupe_stacks)
    print(f'Part 1: {create_word(dupe_stacks)}')

    
    # Part 2 - Apply each move, move all items simultaneously in each move
    dupe_stacks = deepcopy(stacks)
    for move in moves:
        move.apply_9001(dupe_stacks)
    print(f'Part 2: {create_word(dupe_stacks)}')