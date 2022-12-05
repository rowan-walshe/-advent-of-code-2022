from typing import List


INPUT = "day1-input.txt"


class Elf:
    def __init__(self, meals: List[str]) -> None:
        self.__meals = [int(x) for x in meals]
        self.__total_calories = sum(self.__meals)

    @property
    def total_calories(self) -> int:
        return self.__total_calories


class ElfFactory:

    @staticmethod
    def create_elves(file_path: str) -> List[Elf]:
        # Parse file to create list of Elves
        with open(file_path, 'r') as f:
            lines = f.readlines()
        elves = []
        current_meals = []
        for l in lines:
            if l == '\n':
                elves.append(Elf(current_meals))
                current_meals = []
            else:
                current_meals.append(l)
        return elves


if __name__ == "__main__":
    # Parse input
    elves = ElfFactory.create_elves(INPUT)

    # Part 1 - Find the elf carrying the largest number of calories
    max_calories = max([x.total_calories for x in elves])
    print(f'Part 1: {max_calories}')

    # Part 2 - Sum together the top three calorie counts
    sorted_elves = sorted(elves, key=lambda x: x.total_calories, reverse=True)
    top_3 = sum([x.total_calories for x in sorted_elves[:3]])
    print(f'Part 2: {top_3}')