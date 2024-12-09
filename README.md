# Advent of code 2024

## Prerequisites

* uv
* Python 3.13

## Development

Run DuckDB in interactive mode:

```
uv run duckdb
```

Run unit tests using sample inputs:

```
uv run pytest
```

Run python and SQL linters:

```
uvx ruff check .
uvx sqlfluff lint . 
```

## Solutions

Run code to print solutions to sdout:

```
uv run advent_of_code
```

## Packaging?

If you want to build a Python wheel that can be shared with others or published on PyPI:

```
uv build
```