# 37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row. Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],
#                 ["6",".",".","1","9","5",".",".","."],
#                 [".","9","8",".",".",".",".","6","."],
#                 ["8",".",".",".","6",".",".",".","3"],
#                 ["4",".",".","8",".","3",".",".","1"],
#                 ["7",".",".",".","2",".",".",".","6"],
#                 [".","6",".",".",".",".","2","8","."],
#                 [".",".",".","4","1","9",".",".","5"],
#                 [".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],
#         ["6","7","2","1","9","5","3","4","8"],
#         ["1","9","8","3","4","2","5","6","7"],
#         ["8","5","9","7","6","1","4","2","3"],
#         ["4","2","6","8","5","3","7","9","1"],
#         ["7","1","3","9","2","4","8","5","6"],
#         ["9","6","1","5","3","7","2","8","4"],
#         ["2","8","7","4","1","9","6","3","5"],
#         ["3","4","5","2","8","6","1","7","9"]]
import numpy as ny
class Solution:
    def display(self, strBoard: list[list[str]]) -> None:
        # print(strBoard)
        board = ny.matrix(strBoard)
        print(board)

    def checkCondition(self, intBoard, row, column, num):
        for index in range(9):
            if intBoard[row][index] == num or intBoard[index][column] == num:
                return False

        startRow, startColumn = row - row % 3, column - column % 3

        for rowindex in range(3):
            for colindex in range(3):
                if intBoard[rowindex + startRow][colindex + startColumn] == num:
                    return False
        
        return True

    def solveSudoku(self, intBoard, row, column):
        if row == 9 - 1 and column == 9:
            return True

        if column == 9:
            return self.solveSudoku(intBoard, row + 1, 0)
        
        if intBoard[row][column] != 0:
            return self.solveSudoku(intBoard, row, column + 1)           

        for number in range(1,10):
            if self.checkCondition(intBoard, row, column, number):
                intBoard[row][column] = number
                if self.solveSudoku(intBoard, row, column + 1):
                    return True
            intBoard[row][column] = 0

sol = Solution()
strBoard = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
# board = []
# for row in range(9):
#     nums = list(map(int, input(f"Enter The 9 Input Numbers For {row + 1} Row Of Sudoku. Use 0 To Insert Instead Of Blanks. Seperate Each Input From Single Space: ").strip().split()))[:9]
#     board.append(nums)
intBoard = [[int(value) if value != "." else 0 for value in row] for row in strBoard]
if sol.solveSudoku(intBoard, 0, 0):
    strBoard = [[str(value) for value in row] for row in intBoard]
    sol.display(strBoard)
else:
    print("Invalid! Sudoku.")