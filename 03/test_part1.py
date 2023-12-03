from part1 import find_up_row, find_down_row
from textwrap import dedent


def test_find_up_above():
    assert find_up_row(
        data=dedent("""
            ...*......
            ..35..633.
        """).strip(),
        cur_pos=12
    ) == '*'

def test_find_up_outofbounds():
    assert find_up_row(
        data=dedent("""
            ...*......
            ..35..633.
        """).strip(),
        cur_pos=50
    ) == '.'

def test_find_down_below():
    assert find_down_row(
        data=dedent("""
            467..114..
            ...*......
        """).strip().replace('\n', ''),
        cur_pos=2
    ) == '*'

def test_find_down_below_left():
    assert find_down_row(
        data=dedent("""
            ......755.
            ...$.*....
        """).strip().replace('\n', ''),
        cur_pos=6
    ) == '*'

def test_find_down_outofbounds():
    assert find_down_row(
        data=dedent("""
            467..114..
            ...*......
        """).strip().replace('\n', ''),
        cur_pos=50
    ) == '.'

# def test_find_():
#     assert find_down(
#         data=dedent("""
#             467..114..
#             ...*......
#         """).strip().replace('\n', ''),
#         cur_pos=2
#     ) == '*'
#     assert find_down(
#         data=dedent("""
#             467..114..
#             ...*......
#         """).strip().replace('\n', ''),
#         cur_pos=50
#     ) == '.'