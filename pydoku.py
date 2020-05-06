import copy
import puzzles


def get_limits(pos):
    if pos < 3:
        return 0, 3
    if pos < 6:
        return 3, 6
    else:
        return 6, 9


def get_col(solution, col):
    return [row[col] for row in solution]


def get_cube(solution, row, col):
    start_row, end_row = get_limits(row)
    start_col, end_col = get_limits(col)

    return [
        value for row in solution[start_row:end_row] for value in row[start_col:end_col]
    ]


def get_max_count(solution):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for row in solution:
        for col in row:
            counts[col] += 1
    return counts.index(max(counts[1:]))


def check_location(solution, value, row, col):
    if solution[row][col] == 0:
        if value in solution[row]:
            return False
        if value in get_col(solution, col):
            return False
        if value in get_cube(solution, row, col):
            return False
        return True
    return False


def get_possible_values(solution):
    possible_values = [[[] for _ in range(0, 9)] for _ in range(0, 9)]
    for i, row in enumerate(solution):
        for j, value in enumerate(row):
            for k in range(1, 10):
                if check_location(solution, k, i, j):
                    possible_values[i][j].append(k)
    return possible_values


def count_values(solution):
    return sum([1 for row in solution for value in row if value > 0])


def build_possible_solutions(solution, possible_values):
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


def solver(puzzle, solution=None):
    did_update = False
    solution = solution if solution else copy.deepcopy(puzzle)

    if count_values(solution) == 81:
        return solution

    possible_values = get_possible_values(solution)

    for i, row in enumerate(possible_values):
        for j, values in enumerate(row):
            if len(values) == 1:
                solution[i][j] = values[0]
                did_update = True

    if did_update:
        return solver(puzzle, solution)

    possible_solutions = build_possible_solutions(solution, possible_values)
    for possible_solution in possible_solutions:
        try:
            response = solver(puzzle, possible_solution)
            if response:
                return response
        except RecursionError:
            pass


def main(puzzle):
    solution = solver(puzzle)
    for row in solution:
        print(row)


if __name__ == "__main__":
    main(puzzles.expert_puzzle)
