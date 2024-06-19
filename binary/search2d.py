# Search 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) , len(matrix[0]) 

        top, bot = 0, ROWS - 1 
        while top <= bot:
            row = (top + bot) // 2 
            if target < matrix[row][0]:
                bot = row - 1 
            elif target > matrix[row][-1]:
                top = row + 1 
            else:
                break 

        if not (top <= bot):
            return False 

        l, r = 0, COLS - 1 
        row = (top + bot) // 2 
        while l <= r:
            mid = (l + r) // 2 
            if target < matrix[row][mid]:
                r = mid - 1 
            elif target > matrix[row][mid]:
                l = mid + 1 
            else:
                return True 
        return False 
