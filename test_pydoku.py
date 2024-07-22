import pytest

from pydoku import (
    get_col,
    get_cube,
    check_location,
    solver,
    count_values,
)

import puzzles


@pytest.fixture
def easy_puzzle():
    return puzzles.easy_puzzle


@pytest.fixture
def easy_solution():
    return puzzles.easy_solution


def test_get_col(easy_puzzle):
    assert get_col(easy_puzzle, 0) == [0, 0, 7, 8, 0, 0, 0, 4, 2]
    assert get_col(easy_puzzle, 4) == [7, 0, 2, 3, 6, 0, 0, 9, 0]


def test_get_cube(easy_puzzle):
    assert get_cube(easy_puzzle, 0, 0) == [0, 1, 2, 0, 0, 0, 7, 5, 9]
    assert get_cube(easy_puzzle, 8, 5) == [1, 0, 0, 0, 9, 0, 6, 0, 7]


def test_check_location(easy_puzzle):
    assert check_location(easy_puzzle, 7, 1, 7)
    assert not check_location(easy_puzzle, 7, 1, 1)


def test_count_values(easy_puzzle, easy_solution):
    assert count_values(easy_puzzle) == 37
    assert count_values(easy_solution) == 81


@pytest.mark.parametrize(
    "puzzle,solution",
    [
        (puzzles.easy_puzzle, puzzles.easy_solution),
        (puzzles.hard_puzzle, puzzles.hard_solution),
        (puzzles.expert_puzzle, puzzles.expert_solution),
        (puzzles.expert_puzzle2, puzzles.expert_solution2),
    ],
)
def test_solver(puzzle, solution):
    assert solver(puzzle) == solution
