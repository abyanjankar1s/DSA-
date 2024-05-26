# Max Water Container
# Solved 
# You are given an integer array heights where heights[i] represents the height of the 𝑖𝑡ℎ ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l , r = 0, len(heights) - 1 

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res 
    