# Pydoku
## A Sudoku puzzle solver written in Python

### Description
This currently works on easy to hard level sudoku puzzles, but fails at expert level. I know the issue is with multi level possible solutions, but haven't found a clever solution yet. Given this, it may also fail at some hard level puzzles as this is not a complete solver at this time.

### Setup
* `python3.8 -m venv ./venv`
* `pip install -r requirements.txt`

### Test
* `pytest .`  
1 Failing Test - `test_solver_expert()`

### Todo
* Debug why expert puzzle is failing
* Speed things up