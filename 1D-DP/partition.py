# Partition Equal Subset Sum
# Solved 
# You are given an array of positive integers nums.

# Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

# Example 1:

# Input: nums = [1,2,3,4]

# Output: true 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set() 
        dp.add(0) 
        target = sum(nums) // 2 

        for n in nums:
            newDp = set() 
            for t in dp:
                if target == n+t:
                    return True 
                newDp.add(n+t) 
                newDp.add(t) 
            dp = newDp 
        return False 