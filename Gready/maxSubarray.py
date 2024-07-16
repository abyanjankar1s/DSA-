# Maximum Subarray
# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [2,-3,4,-2,2,1,-1,4]

# Output: 8 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] 
        currSum = 0 

        for n in nums:
            if currSum < 0:
                currSum = 0 
            currSum += n 
            maxSub = max(maxSub, currSum) 
        return maxSub 