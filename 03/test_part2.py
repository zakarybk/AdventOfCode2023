from part2 import find_at_pos, full_number


# def test_finds_full_number():
#     assert find_at_pos("this1234", 4) == '1234'
#     assert find_at_pos("this1234what", 4) == '1234'


def test_finds_fuller_number():
    assert full_number("467..114..", 0, 10) == '467'
    assert full_number("467..114..", 1, 10) == '467'
    assert full_number("467..114..", 2, 10) == '467'

def test_finds_number():
    assert find_at_pos("467..114..", 0, 10) == '467'
    assert find_at_pos("467..114..", 1, 10) == '467'
    assert find_at_pos("467..114..", 2, 10) == '467'
    assert find_at_pos("467..114..", 3, 10) == '.'