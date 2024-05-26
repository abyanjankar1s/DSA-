# Trapping Rain Water
# You are given an array non-negative integers heights which represent an elevation map. Each value heights[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:
# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        res = 0
        l , r = 0, len(height) - 1 
        maxL , maxR = height[l], height[r]

        while l < r:
            if maxL > maxR:
                r -= 1 
                maxR = max(maxR, height[r])
                res += maxR - height[r] 
            else:
                l += 1 
                maxL = max(maxL, height[l])
                res += maxL - height[l]
        return res 