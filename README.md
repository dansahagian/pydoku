# Pydoku
## A Sudoku puzzle solver written in Python

### Description
This solver has successfully solved expert level Sudoku puzzles in a couple of seconds.

### Setup
Strictly speaking, there are no requirements other than the standard library to run the solver.
```shell
python src/pydoku.py
```

### Development Environment
Install uv:
https://docs.astral.sh/uv/

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install `ruff` and `pre-commit`:
```shell
uv tool install ruff
uv tool install pre-commit
```

Make sure these are on your PATH:
```shell
export PATH=$PATH:~/.cargo/bin
export PATH=$PATH:~/.local/bin
```

Create the virtualenv and install dependencies:
```shell
uv sync
pre-commit install
```
