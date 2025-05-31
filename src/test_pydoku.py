import pytest

from .puzzles import (
    easy_puzzle,
    easy_solution,
    expert_puzzle,
    expert_puzzle2,
    expert_solution,
    expert_solution2,
    hard_puzzle,
    hard_solution,
)
from .pydoku import (
    check_location,
    count_values,
    get_col,
    get_cube,
    solver,
)


def test_get_col():
    assert get_col(easy_puzzle, 0) == [0, 0, 7, 8, 0, 0, 0, 4, 2]
    assert get_col(easy_puzzle, 4) == [7, 0, 2, 3, 6, 0, 0, 9, 0]


def test_get_cube():
    assert get_cube(easy_puzzle, 0, 0) == [0, 1, 2, 0, 0, 0, 7, 5, 9]
    assert get_cube(easy_puzzle, 8, 5) == [1, 0, 0, 0, 9, 0, 6, 0, 7]


def test_check_location():
    assert check_location(easy_puzzle, 7, 1, 7)
    assert not check_location(easy_puzzle, 7, 1, 1)


def test_count_values():
    assert count_values(easy_puzzle) == 37
    assert count_values(easy_solution) == 81


@pytest.mark.parametrize(
    "puzzle,solution",
    [
        (easy_puzzle, easy_solution),
        (hard_puzzle, hard_solution),
        (expert_puzzle, expert_solution),
        (expert_puzzle2, expert_solution2),
    ],
)
def test_solver(puzzle, solution):
    assert solver(puzzle) == solution
