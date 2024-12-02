from advent_of_code.year2024.solutions import day1, day2

def test_day1():
    # given
    path = "tests/inputs/day1.txt"

    # when
    result = day1(path)

    # then
    assert result == (11, 31)


def test_day2():
    # given
    path = "tests/inputs/day2.txt"

    # when
    result = day2(path)

    # then
    assert result == 2
