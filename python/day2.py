INPUT = 'day2-input.txt'

P1_SCORES = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3,
}

P2_SCORES = {
    'A X': 0 + 3,
    'A Y': 3 + 1,
    'A Z': 6 + 2,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 0 + 2,
    'C Y': 3 + 3,
    'C Z': 6 + 1,
}

if __name__ == '__main__':
    
    # Common scoring rules:
    #     0 3 6 points for a loss, draw, win respectively
    #     1 2 3 points for playing a rock, paper, scissors respectively

    # Parse input
    with open(INPUT, 'r') as f:
        rounds = [line.strip() for line in f.readlines()]
    
    # Part 1 - Calculate scores where X Y Z stands for rock paper scissors respectively
    round_scores = [P1_SCORES[x] for x in rounds]
    score = sum(round_scores)
    print(f'Part 1: {score}')
    
    # Part 2 - Calculate scores where X Y Z means you lose, draw, win respectively
    round_scores = [P2_SCORES[x] for x in rounds]
    score = sum(round_scores)
    print(f'Part 2: {score}')