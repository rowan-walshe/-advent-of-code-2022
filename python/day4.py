from __future__ import annotations
from typing import Tuple


INPUT = 'day4-input.txt'


class CleaningArea:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def contains(self, other: CleaningArea) -> bool:
        # Returns True if the other cleaning area is a subset of this cleaning area
        return self.start <= other.start and self.end >= other.end
    
    def overlaps(self, other: CleaningArea) -> bool:
        # Returns True if this cleaning area overlaps with the other cleaning area
        return self.start <= other.end and self.end >= other.start


def create_cleaning_areas(line: str) -> Tuple[CleaningArea, CleaningArea]:
    # Creates a CleaningArea object from a id range in the format \d+-\d+,\d+-\d+
    ranges = line.split(',')
    areas = []
    for id_range in ranges:
        (start, end) = id_range.split('-')
        areas.append(CleaningArea(int(start), int(end)))
    return tuple(areas)

if __name__ == '__main__':

    # Parse input
    with open(INPUT, 'r') as f:
        pairs = [create_cleaning_areas(line) for line in f.readlines()]
    
    # Part 1 - Count pairings where one area is the subset of the other
    subset_count = sum(x.contains(y) or y.contains(x) for x,y in pairs)
    print(f'Part 1: {subset_count}')

    
    # Part 2 - Count the pairings of areas that overlap
    overlap_count = sum(x.overlaps(y) for x,y in pairs)
    print(f'Part 2: {overlap_count}')