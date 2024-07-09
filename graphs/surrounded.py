# Surrounded Regions
# You are given a 2-D matrix board containing 'X' and 'O' characters.

# If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

# Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

# Example 1:



# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","O","O","X"],
#   ["X","X","X","O"]
# ]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0]) 

        def dfs(r,c):
            if (r not in range(rows) or
                c not in range(cols) or
                board[r][c] != "O"):
                return
            board[r][c] = "T" 
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0,rows-1] or c in [0,cols-1]):
                    dfs(r,c) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        