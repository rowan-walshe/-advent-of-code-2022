from __future__ import annotations
from typing import Set


INPUT = 'day3-input.txt'


class Bag:
    def __init__(self, contents: str) -> None:
        half = len(contents) // 2
        items = list(contents)
        self.__comp_1 = set(items[:half])
        self.__comp_2 = set(items[half:])
        self.__items = set(items)

        # We should validate the input data to make sure that there is only one duplicate, but I trust advent of code <3
        self.__dupe = self.__comp_1 & self.__comp_2
        (self.__dupe,) = self.__dupe

    @property
    def duplicate_item(self) -> str:
        # Returns the item that appears in both bag compartments
        return self.__dupe
    
    @property
    def items(self) -> Set:
        # Returns a set of all items found in a bag
        return self.__items


def priority(character: str) -> int:
    # We should validate the input data to make sure that there are no invalid characters, but I trust advent of code <3
    character_code = ord(character)
    if ord('a') <= character_code <= ord('z'):
        return character_code - 96
    return character_code - 38


if __name__ == '__main__':

    # Parse input
    with open(INPUT, 'r') as f:
        bags = [Bag(line.strip()) for line in f.readlines()]
    
    # Part 1 - 
    priorities = [priority(bag.duplicate_item) for bag in bags]
    print(f'Part 1: {sum(priorities)}')

    
    # Part 2 - 
    total = 0
    for i in range(0, len(bags), 3):
        duplicate = bags[i].items & bags[i + 1].items & bags[i + 2].items
        # We should validate the input data to make sure that there is only one duplicate, but I trust advent of code <3
        (duplicate,) = duplicate
        total += priority(duplicate)
    print(f'Part 2: {total}')