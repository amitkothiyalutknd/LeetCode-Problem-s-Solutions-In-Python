# 51. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]

class Solution:
    def validation(self, row):
        if row == noOfQueens:
            placement = ["".join(r) for r in self.board]
            self.resultBoard.append(placement)
            return
        
        for column in  range(noOfQueens):
            if column in self.coloums or (row + column) in self.posDiag or (row - column) in self.negDiag:
                continue

            self.coloums.add(column)
            self.posDiag.add(row + column)
            self.negDiag.add(row - column)
            self.board[row][column] = "Q"

            self.validation(row + 1)

            self.coloums.remove(column)
            self.posDiag.remove(row + column)
            self.negDiag.remove(row - column)
            self.board[row][column] = "."


    def solveNQueens(self, n: int) -> list[list[str]]:
        self.board, self.resultBoard = [["."] * n for row in range(n)], []
        self.coloums, self.posDiag, self.negDiag = set(), set(), set()
        self.validation(0)
        return self.resultBoard

sol = Solution()
noOfQueens = int(input("Enter The Number Of Queen To Be Place On Board:"))
print(f"There Is Solution To The {noOfQueens} Puzzle Is:\t", sol.solveNQueens(noOfQueens))