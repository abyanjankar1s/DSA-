# Target Sum
# You are given an array of integers nums and an integer target.

# For each number in the array, you can choose to either add or subtract it to a total sum.

# For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
# If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

# Return the number of different ways that you can build the expression such that the total sum equals target.

# Example 1:

# Input: nums = [2,2,2], target = 2

# Output: 3 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} 

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0 
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]) 
            return dp[(i, total)] 
        return backtrack(0, 0) 