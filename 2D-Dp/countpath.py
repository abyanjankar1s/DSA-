# Count Paths
# There is an m x n grid where you are allowed to move either down or to the right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

# You may assume the output will fit in a 32-bit integer.

# Example 1:



# Input: m = 3, n = 6

# Output: 21
# Example 2:

# Input: m = 3, n = 3

# Output: 6 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n 
        
        for i in range(m-1):
            newRow = [1] * n 
            for j in range(n-2, -1,-1):
                newRow[j] = newRow[j+1] + row[j] 
            row = newRow 
        return row[0] 