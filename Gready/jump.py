# Jump Game
# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.

# Example 1:

# Input: nums = [1,2,0,1,0]

# Output: true 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i 
        return goal == 0 