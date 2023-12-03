import re
import itertools
from pathlib import Path
from typing import Iterable, List, Tuple, Set

num_re = re.compile('\\d+')
gear_re = re.compile('\\*')


def is_number(char: str) -> bool:
    print(char)
    return char.isnumeric()

def is_gear(char: str) -> bool:
    return char == '*'


def full_number(line: str, inline_pos: int, line_length: int):
    start_pos = inline_pos
    # search left for first digit
    for i, char in map(lambda i: (i, line[i]), range(inline_pos, -1, -1)):
        if char.isnumeric():
            start_pos = i
        else:
            break
    # search left to right for full number
    return num_re.search(line, pos=start_pos).group()


def get_line(data: str, pos: int, line_length: int) -> Tuple[str, int]:
    inline_pos = pos % line_length
    line_start = pos - inline_pos
    line_end = line_start + line_length
    return data[line_start:line_end], inline_pos


def find_at_pos(data: str, pos: int, line_length: int) -> str:
    at_pos = pos in range(len(data)) and data[pos] or '.'
    if at_pos.isnumeric():
        line, inline_pos = get_line(data, pos, line_length)
        return full_number(line, inline_pos, line_length)
    return '.'


def all_numbers(iter: Iterable) -> List[str]:
    return list(filter(is_number, iter)) 


def find_left(data: str, cur_pos: int, line_length: int) -> str:
    left_pos = cur_pos - 1
    return find_at_pos(data, left_pos, line_length)

def find_right(data: str, cur_pos: int, line_length: int) -> str:
    right_pos = cur_pos + 1
    return find_at_pos(data, right_pos, line_length)

def find_up_row(data: str, cur_pos: int, line_length: int) -> Set[str]:
    up_pos = cur_pos - line_length
    at_up = find_at_pos(data, up_pos, line_length)
    at_right_pos = find_right(data, up_pos, line_length)
    at_left_pos = find_left(data, up_pos, line_length)
    return set(all_numbers(
        (at_up, at_right_pos, at_left_pos)
    ))

def find_down_row(data: str, cur_pos: int, line_length: int) -> Set[str]:
    down_pos = cur_pos + line_length
    at_down = find_at_pos(data, down_pos, line_length)
    at_right_pos = find_right(data, down_pos, line_length)
    at_left_pos = find_left(data, down_pos, line_length)
    return set(all_numbers(
        (at_down, at_right_pos, at_left_pos)
    ))

def find_around_pos(data: str, cur_pos: int, line_length: int) -> List[str]:
    return all_numbers(
        list(map(
            lambda fn: fn(data, cur_pos, line_length),
            (find_left, find_right)
        )) + list(itertools.chain(
            *map(
                lambda fn: fn(data, cur_pos, line_length),
                (find_up_row, find_down_row)
            )
        ))
    )


def solve_puzzle(data: str, line_length: int):
    total = 0
    for match in gear_re.finditer(data):
        start_index = match.start()
        numbers = find_around_pos(data, start_index, line_length)
        print(f"{numbers} near *")
        if len(numbers) > 1:
            print(numbers[0], numbers[1])
            total += int(numbers[0]) * int(numbers[1])
    return total




if __name__ == '__main__':
    sample_input = Path("sample_input.txt").read_text()
    puzzle_input = Path("input.txt").read_text()

    selected_input = puzzle_input

    line_length = len(selected_input.splitlines()[0])

    single_line_selected_input = selected_input.replace('\n', '')  # search funcs don't expect \n
    # [(m.start(0), m.end(0)) for m in re.finditer(pattern, string)]
    print(solve_puzzle(single_line_selected_input, line_length))