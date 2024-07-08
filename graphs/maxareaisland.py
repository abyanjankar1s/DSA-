# Max Area of Island
# Solved 
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:

# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]

# Output: 6 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        visit = set() 

        def dfs(r,c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or
                (r,c) in visit):
                return 0 
            
            visit.add((r,c)) 
            res = (1 + dfs(r+1,c)+
                        dfs(r-1,c)+
                        dfs(r,c+1)+
                        dfs(r,c-1)) 
            return res 
        
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area 