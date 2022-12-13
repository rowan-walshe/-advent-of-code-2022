from __future__ import annotations
from enum import Enum
from typing import List, Optional, Tuple, TypedDict

INPUT = 'day9-input.txt'


class Direction(Enum):
    U = (0,1)
    R = (1,0)
    D = (0,-1)
    L = (-1,0)


class Move(TypedDict):
    direction: Direction
    times: int


class Knot:
    def __init__(self, child: Optional[Knot] = None) -> None:
        self.pos = (0, 0)
        self.child = child
        self.visited = set()
        self.visited.add((0, 0))
    
    def _apply_move(self, direction: Tuple[int, int]):
        # Move this knot by direction, and update child if one exists
        self.pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])
        self.visited.add(self.pos)
        
        if self.child is not None:
            difference = (self.child.pos[0] - self.pos[0], self.child.pos[1] - self.pos[1])
            if 2 in difference or -2 in difference:
                move = []
                for i in difference:
                    if i < 0:
                        move.append(1)
                    elif i > 0:
                        move.append(-1)
                    else:
                        move.append(0)
                self.child._apply_move((move[0], move[1]))
    
    def apply_move(self, move: Move):
        # Apply a single of move to this knot
        for i in range(move['times']):
            self._apply_move(move['direction'].value)
    
    def apply_moves(self, moves: List[Move]):
        # Apply a list of moves to this knot
        for move in moves:
            self.apply_move(move)


def create_moves(lines: List[str]) -> List[Move]:
    split = [l.split() for l in lines]
    return [Move(direction=Direction[a], times=int(b)) for a,b in split]


if __name__ == "__main__":
    with open(INPUT, 'r') as f:
        lines = f.readlines()

    moves = create_moves(lines)
    

    # Part 1 - Apply moves to a rope with 2 knots
    tail = Knot()
    head = Knot(tail)    
    head.apply_moves(moves)
    print(f'Part 1: {len(tail.visited)}')

    # Part 2 Apply moves to a rope with 10 knots
    rope = [Knot()]
    for i in range(9):
        rope.append(Knot(rope[i]))
    rope[-1].apply_moves(moves)
    print(f'Part 2: {len(rope[0].visited)}')
