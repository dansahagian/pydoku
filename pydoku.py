import copy


def get_limits(pos: int) -> (int, int):
    if pos < 3:
        return 0, 3
    if pos < 6:
        return 3, 6
    else:
        return 6, 9


def get_col(solution: list[list], col: int) -> list:
    return [row[col] for row in solution]


def get_cube(solution: list[list], row: int, col: int) -> list:
    start_row, end_row = get_limits(row)
    start_col, end_col = get_limits(col)

    return [
        value for row in solution[start_row:end_row] for value in row[start_col:end_col]
    ]


def check_location(solution: list[list], value: int, row: int, col: int) -> bool:
    if solution[row][col] == 0:
        if value in solution[row]:
            return False
        if value in get_col(solution, col):
            return False
        if value in get_cube(solution, row, col):
            return False
        return True
    return False


def get_possible_values(solution: list[list]):
    possible_values = [[[] for _ in range(0, 9)] for _ in range(0, 9)]
    for i, row in enumerate(solution):
        for j, value in enumerate(row):
            for k in range(1, 10):
                if check_location(solution, k, i, j):
                    possible_values[i][j].append(k)
    return possible_values


def count_values(solution: list[list]) -> int:
    return sum([1 for row in solution for value in row if value > 0])


def is_solution_valid(solution: list[list]) -> bool:
    for row in solution:
        row_value_counts = [0 for _ in range(0, 10)]
        for value in row:
            row_value_counts[value] += 1
        if max(row_value_counts[1:]) > 1:
            return False

    for col in range(0, 9):
        col_value_counts = [0 for _ in range(0, 10)]
        for value in get_col(solution, col):
            col_value_counts[value] += 1
        if max(col_value_counts[1:]) > 1:
            return False

    return True


def build_possible_solutions(solution: list[list], possible_values: list[list[list]]):
    twofers = []
    for i, row in enumerate(possible_values):
        for j, values in enumerate(row):
            if len(values) == 2:
                twofers.append((values, i, j))

    solutions = [solution]
    for twofer in twofers:
        values, row, col = twofer
        n = len(solutions)
        for s in solutions:
            if check_location(s, values[0], row, col):
                s0 = copy.deepcopy(s)
                s0[row][col] = values[0]
                solutions.append(s0)
            if check_location(s, values[1], row, col):
                s1 = copy.deepcopy(s)
                s1[row][col] = values[1]
                solutions.append(s1)
        solutions = solutions[n:]
    return solutions


def solver(solution: list[list]) -> list[list] | None:
    if not is_solution_valid(solution):
        return None

    if count_values(solution) == 81:
        return solution

    did_update = False
    possible_values = get_possible_values(solution)

    for i, row in enumerate(possible_values):
        for j, values in enumerate(row):
            if len(values) == 1:
                solution[i][j] = values[0]
                did_update = True

    if did_update:
        return solver(solution)

    possible_solutions = build_possible_solutions(solution, possible_values)
    for possible_solution in possible_solutions:
        try:
            response = solver(possible_solution)
            if response:
                return response
        except RecursionError:
            pass


def printer(solution: list[list]):
    print()
    for row in solution:
        r = [(lambda x: str(x) if x > 0 else " ")(x) for x in row]
        print(f"| {' | '.join(r)} |")
        print("-" * 37)
    print()


def preamble() -> None:
    print("\nHello! Hopefully I can help you solve your Sudoku puzzle.")
    print("I will have you enter your puzzle row by row.")
    print("Please use 0 as an empty and spaces between cells.")
    print("An example row might look like this: 4 0 3 0 0 0 7 0 0.\n")


def main() -> None:
    preamble()

    puzzle = []
    for i in range(0, 9):
        data = input(f"Please enter row {i + 1}: ")
        row = [int(x) for x in data.split()]
        puzzle.append(row)

    print("Before I begin, is this the puzzle you want me to solve?\n")
    printer(puzzle)

    answer = input("y/n: ")
    return printer(solver(puzzle)) if answer == "y" else main()


if __name__ == "__main__":
    main()
