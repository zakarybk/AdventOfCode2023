import operator
from functools import reduce
from pathlib import Path

cube_count = {
    'red': 12,
    'green': 13,
    'blue': 14
}

test_input = Path("test_input.txt").read_text().splitlines()
puzzle_input = Path("input.txt").read_text().splitlines()

cum_possible = 0

for game in puzzle_input:
    maxes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    game_num = int(game.split(':')[0].replace('Game ', ''))
    game_rounds = game.split(':')[1].split(';')
    for game_round in game_rounds:
        for hand in game_round.split(','):
            count, colour = hand.strip().split(' ')
            maxes[colour] = max(maxes[colour], int(count))

    cum_possible += reduce(operator.mul, maxes.values())

print(f"cum: {cum_possible}")