# Subsets II
# You are given an array nums of integers, which that may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,1]

# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]] 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort() 

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::]) 
                return 
            
            subset.append(nums[i]) 
            backtrack(i+1, subset) 
            subset.pop() 

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1 
            backtrack(i+1, subset) 
            
        backtrack(0, []) 
        return res 