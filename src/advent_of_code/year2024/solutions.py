import duckdb


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


def day2(path: str) -> int:
    with open("src/advent_of_code/year2024/day2_part1.sql", "r") as file:
        query1 = file.read()
    
    query1 = query1.replace("{{ path }}", path)
    part1 = duckdb.query(query1).fetchone()[0]

    return part1
