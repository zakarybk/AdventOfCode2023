from pathlib import Path
from typing import List, Tuple
from functools import reduce
import re

card_re = re.compile('Card\\s+(\\d+):(.*)\\|(.*)')

test_input = Path("sample_input2.txt").read_text().splitlines()
puzzle_input = Path("input.txt").read_text().splitlines()

def parse_card(card: str) -> Tuple[int, List[int], List[int]]:
    """ (card num, winning numbers, have numbers) """
    match = card_re.match(card)
    filt_empty = lambda x: x != ''
    return (
        int(match.group(1)),
        list(map(int, filter(filt_empty, match.group(2).split(' ')))),
        list(map(int, filter(filt_empty, match.group(3).split(' ')))),
    )

def solve(puzzle: List[str]) -> int:
    card_counts = {i: 1 for i in range(1, len(puzzle)+1)}

    for num, winning, have in map(parse_card, puzzle):
        same = set(winning).intersection(set(have))
        for i in range(num+1, num+1+len(same)):
            card_counts[i] += card_counts[num]

    return sum(card_counts.values())

print(solve(puzzle_input))

