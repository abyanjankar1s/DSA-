# Rotting Fruit
# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every second, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of seconds that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

# Example 1:

# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

# Output: 4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        time, fresh = 0, 0
        q = deque() 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c]) 
                if grid[r][c] == 1:
                    fresh += 1 
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr,dc in direction:
                    row,col = r+dr, c+dc
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col]==1):
                        q.append([row,col])
                        grid[row][col] = 2 
                        fresh -= 1 
            time += 1 
        return time if fresh == 0 else -1 
