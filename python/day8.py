from typing import List, TypedDict

class GridSpot(TypedDict):
    value: int
    visible : bool
    north : int
    east : int
    south : int
    west : int
    score : int

INPUT = 'day8-input.txt'

def create_grid_spot(value: int) -> GridSpot:
    return GridSpot(
        value=value,
        visible=False,
        north=0,
        east=0,
        south=0,
        west=0,
        score=0
    )


def update_scenic_score(x: int, y: int, grid: List[List[GridSpot]]):
    height = len(grid)
    width = len(grid[0])

    north = 0
    east = 0
    south = 0
    west = 0

    current = grid[x][y]

    # Count trees that can be seen north
    for i in range(x-1, -1, -1):
        new = grid[i][y]
        north += 1
        if new['value'] >= current['value']:
            break

    # Count trees that can be seen east
    for j in range(y+1, width):
        new = grid[x][j]
        east += 1
        if new['value'] >= current['value']:
            break

    # Count trees that can be seen south
    for i in range(x+1, height):
        new = grid[i][y]
        south += 1
        if new['value'] >= current['value']:
            break

    # Count trees that can be seen west
    for j in range(y-1, -1, -1):
        new = grid[x][j]
        west += 1
        if new['value'] >= current['value']:
            break
    
    current['score'] = north * east * south * west


def create_grid(raw_grid: List[List[int]]) -> List[List[GridSpot]]:
    # Create initial grid
    grid = [[create_grid_spot(x) for x in row] for row in raw_grid]
    height = len(grid)
    width = len(grid[0])

    # Update grid from north to south
    for spot in grid[0]:
        spot['visible'] = True
        spot['north'] = spot['value']
    for i in range(1, height):
        for j in range(width):
            current = grid[i][j]
            prev = grid[i-1][j]
            current['visible'] = current['value'] > prev['north']
            current['north'] = max(current['value'], prev['north'])

    # Update grid from east to west
    for row in grid:
        spot = row[-1]
        spot['visible'] = True
        spot['east'] = spot['value']
    for i in range(height):
        for j in range(width-2, -1, -1):
            current = grid[i][j]
            prev = grid[i][j+1]
            current['visible'] = current['visible'] or current['value'] > prev['east']
            current['east'] = max(current['value'], prev['east'])

    # Update grid from south to north
    for spot in grid[-1]:
        spot['visible'] = True
        spot['south'] = spot['value']
    for i in range(height-2, -1, -1):
        for j in range(width):
            current = grid[i][j]
            prev = grid[i+1][j]
            current['visible'] = current['visible'] or current['value'] > prev['south']
            current['south'] = max(current['value'], prev['south'])

    # Update grid from west to east
    for row in grid:
        spot = row[0]
        spot['visible'] = True
        spot['west'] = spot['value']
    for i in range(height):
        for j in range(1, width):
            current = grid[i][j]
            prev = grid[i][j-1]
            current['visible'] = current['visible'] or current['value'] > prev['west']
            current['west'] = max(current['value'], prev['west'])
    

    # Update each spot's scenic score
    for i in range(height):
        for j in range(width):
            update_scenic_score(i, j, grid)

    return grid


def count_visible(grid: List[List[GridSpot]]) -> int:
    count = 0
    for row in grid:
        for spot in row:
            count += spot['visible']
    return count


def max_scenic_score(grid: List[List[GridSpot]]) -> int:
    score = 0
    for row in grid:
        for spot in row:
            score = max(score, spot['score'])
    return score


if __name__ == "__main__":
    with open(INPUT, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    raw_grid = [[int(x) for x in line] for line in lines]
    grid = create_grid(raw_grid)

    # Part 1 - Count trees visible from outside of the forest
    print(f'Part 1: {count_visible(grid)}')

    # Part 2 - Find the tree with the highest scenic score
    print(f'Part 2: {max_scenic_score(grid)}')