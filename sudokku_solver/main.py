from pprint import pprint

unsolved_sudoku = [[-1, -1, -1, -1, -1, -1, -1, -1, 8],
                   [4, -1, 3, 9, -1, 2, -1, -1, -1],
                   [-1, 9, 1, -1, -1, -1, 4, -1, -1],
                   [8, 3, 6, -1, 4, 9, 5, 1, -1],
                   [2, -1, -1, -1, -1, -1, 8, 7, -1],
                   [-1, 7, 9, 8, 2, 5, 6, 4, -1],
                   [-1, -1, -1, -1, 9, 7, 2, -1, 6],
                   [3, -1, -1, -1, -1, -1, 9, -1, -1],
                   [-1, 6, -1, -1, -1, 8, -1, -1, 4]]

# to find the nan value


def find_nan_value(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == -1:
                return r, c
    return None, None


def valid_guess(sudoku, guess, row, col):
    row_values = sudoku[row]
    if guess in row_values:
        return False

    col_values = [sudoku[i][col] for i in range(9)]
    if guess in col_values:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if sudoku[i][j] == guess:
                return False

    return True


def sudoku_solver(sudoku):
    row, col = find_nan_value(sudoku)

    if row is None:
        return True

    for guess in range(1,10):
        if valid_guess(sudoku,guess,row,col):
            sudoku[row][col] = guess

            if sudoku_solver(sudoku):
                return True

        sudoku[row][col] = -1

    return False

sudoku_solver(unsolved_sudoku)
pprint(unsolved_sudoku)
