[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-382/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Pydoku
## A Sudoku puzzle solver written in Python

### Description
This solver has successfully solved expert level Sudoku puzzles in a couple of seconds.

### Setup
Strictly speaking, there are no requirements to run the solver.
If you'd like to use the black formatter or run the tests that you'll want to install the requirements into a virtualenv.
* `python3.9 -m venv ./venv`
* `pip install -r requirements.txt`

### Tests
* `pytest .`  

### Todo
* Look into a better grid/entry
* Write some more test coverage
* Speed things up