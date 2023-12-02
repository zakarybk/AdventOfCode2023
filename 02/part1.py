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
    gg = True
    game_num = int(game.split(':')[0].replace('Game ', ''))
    game_rounds = game.split(':')[1].split(';')
    for game_round in game_rounds:
        for hand in game_round.split(','):
            count, colour = hand.strip().split(' ')
            if int(count) > cube_count[colour]:
                gg = False
                break
    if gg:
        cum_possible += game_num

print(f"cum: {cum_possible}")