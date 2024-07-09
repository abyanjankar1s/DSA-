# Islands and Treasure
# Solved 
# You are given a 
# 𝑚
# ×
# 𝑛
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ] 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0]) 
        visit = set() 
        q = deque() 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c]) 
                    visit.add((r,c)) 
        
        def addVal(r,c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == -1 or
                (r,c) in visit):
                return 
            q.append([r,c])
            visit.add((r,c)) 

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance 
                addVal(r+1,c)
                addVal(r-1,c)
                addVal(r,c+1)
                addVal(r,c-1) 
            distance += 1 