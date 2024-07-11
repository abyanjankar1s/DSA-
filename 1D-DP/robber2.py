# House Robber II
# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

# Example 1:

# Input: nums = [3,4,3]

# Output: 4 

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) 
    
    def helper(self, nums):
        rob1, rob2 = 0, 0 
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2 