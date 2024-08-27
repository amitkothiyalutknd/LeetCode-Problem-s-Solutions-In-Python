# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# | ⓐ | ⓑ | ⓒ | e |
# -------------------
# | s  | f  | ⓒ | s |
# -------------------
# | a  | ⓓ | ⓔ | e |
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# | a | b |  c | e  |
# -------------------
# | s | f |  c | ⓢ |
# -------------------
# | a | d | ⓔ | ⓔ |
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# | a | b | c | e |
# -----------------
# | s | f | c | s |
# -----------------
# | a | d | e | e | 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution:
    def dfs(self, board, word, visited, i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j]!= word[k]:
            return False
        visited[i][j] = True
        res = self.dfs(board, word, visited, i-1, j, k+1) or self.dfs(board, word, visited, i+1, j, k+1) or self.dfs(board, word, visited, i, j-1, k+1) or self.dfs(board, word, visited, i, j+1, k+1)
        visited[i][j] = False
        return res

    def exist(self, board:list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, visited, i, j, 0):
                    return True
        return False

sol = Solution()
row, col = (map(int, input("Enter The Number Of Rows and Columns. Separate Both Inputs from Single Space.:\t").split(' ')))
board = []
for i in range(row):
    board.append(list(map(str, input(f"Enter {col} values of {i+1} rows. Separate Each Inputs from Single Space.:\t").upper().split(' '))))
word = input('Enter The Word To Be Search:\t').upper()
print(sol.exist(board, word))