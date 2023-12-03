import re
from pathlib import Path
from typing import Iterable

def is_symbol(char: str) -> bool:
    return not char.isnumeric() and char != '.'

def find_at_pos(data: str, pos: int) -> str:
    return pos in range(len(data)) and data[pos] or '.'

def first_symbol(iter: Iterable) -> str:
    return next(
        filter(
            is_symbol,
            iter
        ),
        '.'
    )

def find_left(data: str, cur_pos: int, line_length=10) -> str:
    left_pos = cur_pos - 1
    return find_at_pos(data, left_pos)

def find_right(data: str, cur_pos: int, line_length=10) -> str:
    right_pos = cur_pos + 1
    return find_at_pos(data, right_pos)

def find_up_row(data: str, cur_pos: int, line_length=10) -> str:
    up_pos = cur_pos - line_length
    at_up = find_at_pos(data, up_pos)
    at_right_pos = find_right(data, up_pos, line_length)
    at_left_pos = find_left(data, up_pos, line_length)
    return first_symbol(
        (at_up, at_right_pos, at_left_pos)
    )

def find_down_row(data: str, cur_pos: int, line_length=10) -> str:
    down_pos = cur_pos + line_length
    at_down = find_at_pos(data, down_pos)
    at_right_pos = find_right(data, down_pos, line_length)
    at_left_pos = find_left(data, down_pos, line_length)
    return first_symbol(
        (at_down, at_right_pos, at_left_pos)
    )

def find_around_pos(data: str, cur_pos: int, line_length=10) -> str:
    return first_symbol(
        map(
            lambda fn: fn(data, cur_pos, line_length),
            (find_left, find_right, find_up_row, find_down_row)
        )
    )

def find_around_num(data: str, num: int, cur_pos: int, line_length=10):
    return first_symbol(
        map(
            lambda i: find_around_pos(data, cur_pos+i, line_length),
            range(len(str(num)))
        )
    )

def solve_puzzle(data: str, line_length=10):
    total = 0
    num_re = re.compile('\\d+')
    for match in num_re.finditer(data):
        start_index = match.start()
        num = int(match.group())
        symbol = find_around_num(data, num, start_index, line_length)
        print(f"{num} near {symbol}")
        if symbol != '.':
            total += num
    return total




if __name__ == '__main__':
    sample_input = Path("sample_input.txt").read_text()
    puzzle_input = Path("input.txt").read_text()

    selected_input = puzzle_input

    line_length = len(selected_input.splitlines()[0])

    single_line_selected_input = selected_input.replace('\n', '')  # search funcs don't expect \n
    # [(m.start(0), m.end(0)) for m in re.finditer(pattern, string)]
    print(solve_puzzle(single_line_selected_input, line_length))