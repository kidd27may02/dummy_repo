unsolved_sudoku = [[-1, -1, -1, -1, -1, -1, -1, -1, 8],
                   [4, -1, 3, 9, -1, 2, -1, -1, -1],
                   [-1, 9, 1, -1, -1, -1, 4, -1, -1],
                   [8, 3, 6, -1, 4, 9, 5, 1, -1],
                   [2, -1, -1, -1, -1, -1, 8, 7, -1],
                   [-1, 7, 9, 8, 2, 5, 6, 4, -1],
                   [-1, -1, -1, -1, 9, 7, 2, -1, 6],
                   [3, -1, -1, -1, -1, -1, 9, -1, -1],
                   [-1, 6, -1, -1, -1, 8, -1, -1, 4]]

a = []
for i in range(len(unsolved_sudoku)):
    for j in range(len(unsolved_sudoku)):
        a.append(unsolved_sudoku[i][j])

print(a)

# for i in range(len(unsolved_sudoku)):
#     print(len(unsolved_sudoku[i]))




