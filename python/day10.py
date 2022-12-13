from typing import List


INPUT = 'day10-input.txt'


class CPU:
    def __init__(self) -> None:
        self.cycles = [1]
        self.cycle = 1
        self.x = 1
        self.image = []
    
    def _update_image(self):
        # Update image and cycle number
        if self.x - 1 <= (self.cycle-1) % 40 <= self.x + 1:
            self.image.append('#')
        else:
            self.image.append('.')
        self.cycle += 1

    def run(self, program: List[str]):
        # Run program
        for l in program:
            if l.startswith('noop'):
                self._update_image()
                self.cycles.append(self.x)
            else:
                self._update_image()
                self.cycles.append(self.x)
                self._update_image()
                self.cycles.append(self.x)
                self.x += int(l.split(' ')[1])

if __name__ == "__main__":
    with open(INPUT, 'r') as f:
        lines = f.readlines()
    cpu = CPU()
    cpu.run(lines)

    # Part 1 - Sum cycle num * cycle value for a number of cycle numbers
    result = 20 * cpu.cycles[20]
    result += 60 * cpu.cycles[60]
    result += 100 * cpu.cycles[100]
    result += 140 * cpu.cycles[140]
    result += 180 * cpu.cycles[180]
    result += 220 * cpu.cycles[220]
    print(f'Part 1: {result}')

    # Part 2 - Print image produced by program
    for i in range(0, 240, 40):
        print(''.join(cpu.image[i:i+40]))
