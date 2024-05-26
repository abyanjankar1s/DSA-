# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)
        longest = 0

        for n in newNums:
            if (n - 1) not in newNums:
                length = 1
                while n + length in newNums:
                    length += 1
                    longest = max(length, longest)
        return longest 