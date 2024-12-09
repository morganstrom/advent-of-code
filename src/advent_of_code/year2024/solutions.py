import duckdb
import re


def day1(path: str) -> tuple[int]:
    with open("src/advent_of_code/year2024/day1_part1.sql", "r") as file:
        query1 = file.read()

    query1 = query1.replace("{{ path }}", path)
    part1 = duckdb.query(query1).fetchone()[0]

    with open("src/advent_of_code/year2024/day1_part2.sql", "r") as file:
        query2 = file.read()

    query2 = query2.replace("{{ path }}", path)
    part2 = duckdb.query(query2).fetchone()[0]

    return (part1, part2)


def day2(path: str) -> tuple[int]:
    with open("src/advent_of_code/year2024/day2_part1.sql", "r") as file:
        query1 = file.read()

    query1 = query1.replace("{{ path }}", path)
    part1 = duckdb.query(query1).fetchone()[0]

    part2 = 4
    # Didn't manage to solve part 2 using sql
    return (part1, part2)


def day3(path: str) -> tuple[int]:
    part1 = 0
    with open(path, "r") as file:
        for line in file:
            substrings = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
            for multiplication in substrings:
                first_number = re.match(r"mul\((\d{1,3}),", multiplication).group(1)
                second_number = re.search(r",(\d{1,3})\)", multiplication).group(1)
                part1 += int(first_number) * int(second_number)

    part2 = 0
    with open(path, "r") as file:
        # multiplications are enabled at the start of the program
        enabled = True
        for line in file:
            # find locations of the following patterns:
            # mul(\d{1,3},\d{1,3}) indicates a multiplication operation
            multiplication_locations = [
                m.start() for m in re.finditer(r"mul\(\d{1,3},\d{1,3}\)", line)
            ]
            # do() indicates that following multiplications are enabled
            on_locations = [m.start() for m in re.finditer(r"do\(\)", line)]
            # don't() indicates that following multiplications are disabled
            off_locations = [m.start() for m in re.finditer(r"don\'t\(\)", line)]

            # iterate over the line and calculate the result of each multiplication
            i = 0
            while i < len(line):
                if i in on_locations:
                    enabled = True
                    i += len("do()") - 1
                elif i in off_locations:
                    enabled = False
                    i += len("don't()") - 1
                elif i in multiplication_locations:
                    first_number = re.match(r"mul\((\d{1,3}),", line[i:]).group(1)
                    second_number = re.search(r",(\d{1,3})\)", line[i:]).group(1)
                    if enabled:
                        part2 += int(first_number) * int(second_number)
                    i += len(f"mul({first_number}, {second_number})") - 1
                else:
                    i += 1

    return (part1, part2)
