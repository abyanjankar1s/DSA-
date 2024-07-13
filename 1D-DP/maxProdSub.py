# Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product within the array and return it.

# A subarray is a contiguous non-empty sequence of elements within an array.

# You can assume the output will fit into a 32-bit integer.

# Example 1:

# Input: nums = [1,2,-3,4]

# Output: 4

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        maxV, minV = 1, 1 

        for n in nums:
            temp = maxV * n 
            maxV = max(n, maxV*n, minV*n) 
            minV = min(n, temp, minV*n) 
            res = max(res, maxV) 
        return res 
    
