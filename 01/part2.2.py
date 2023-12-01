from pathlib import Path
from typing import List
import re


written_nums = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
written_nums_to_str = {k: str(i + 1) for i, k in enumerate(written_nums)}
num_pattern = re.compile("\\d+")


def first_and_last(line: str) -> int:
    word = ""
    first_num, last_num = None, None

    for char in line:
        word += char
        for num in (*written_nums_to_str.keys(), *written_nums_to_str.values()):
            if num in word:
                if num in written_nums:
                    first_num = written_nums_to_str[num]
                else:
                    first_num = num
                break
        if first_num:
            break

    word = ""

    for char in reversed(line):
        word = char + word
        for num in (*written_nums_to_str.keys(), *written_nums_to_str.values()):
            if num in word:
                if num in written_nums:
                    last_num = written_nums_to_str[num]
                else:
                    last_num = num
                break
        if last_num:
            break

    return int(f"{first_num}{last_num}")


def puzzle_answer(data: List[str]) -> int:
    return sum(map(first_and_last, data))


if __name__ == "__main__":
    raw_data = Path("input.txt").read_text().splitlines()
    answer = puzzle_answer(raw_data)
    print(f"Try this: {answer}")
