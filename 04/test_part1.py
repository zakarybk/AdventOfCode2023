from part1 import parse_card


def test_parse_card():
    assert (
        parse_card("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
        ==
        (6, [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
    )