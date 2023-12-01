from pathlib import Path
from typing import List
import re
from re import Pattern


def reverse(line: str) -> str:
    return line[::-1]


written_nums = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
written_num_matchers = [re.compile(num) for num in written_nums]
written_nums_to_str = {k: str(i + 1) for i, k in enumerate(written_nums)}
written_num_pattern = re.compile("|".join(written_nums))
written_num_pattern_reversed = re.compile("|".join(map(reverse, written_nums)))
num_pattern = re.compile("\\d+")


# Doesn't work due to overlapping of numbers / no order checking
def replace_written(line: str) -> str:
    return re.sub(
        pattern=written_num_pattern,
        repl=lambda x: written_nums_to_str[x[0]],
        count=1,
        string=reverse(
            re.sub(
                pattern=written_num_pattern_reversed,
                repl=lambda x: written_nums_to_str[reverse(x[0])],
                string=reverse(line),
                count=1,
            )
        ),
    )


def first_and_last(line: str) -> int:
    nums = num_pattern.findall(line)
    ans = int(f"{nums[0][0]}{nums[-1][-1]}")
    print(f"{line} turned into {ans}")
    return int(f"{nums[0][0]}{nums[-1][-1]}")


def puzzle_answer(data: List[str]) -> int:
    return sum(map(first_and_last, map(replace_written, data)))


if __name__ == "__main__":
    raw_data = Path("input.txt").read_text().splitlines()
    answer = puzzle_answer(raw_data)
    print(f"Try this: {answer}")
