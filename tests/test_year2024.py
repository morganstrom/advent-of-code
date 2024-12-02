from advent_of_code.year2024.solutions import day1

def test_day1():
    # given
    path = "tests/inputs/day1.txt"

    # when
    result = day1(path)

    # then
    assert result == (11, 31)
