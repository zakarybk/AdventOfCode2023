from pathlib import Path
from typing import List, Tuple
from functools import reduce
import re

card_re = re.compile('Card\\s+(\\d+):(.*)\\|(.*)')

test_input = Path("sample_input.txt").read_text().splitlines()
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
    total = 0
    for card in puzzle:
        num, winning, have = parse_card(card)
        same = set(winning).intersection(set(have))
        total += len(same) > 1 and reduce(lambda x,y: x*2, range(1,len(same)+1)) or len(same)
    return total

print(solve(puzzle_input))

