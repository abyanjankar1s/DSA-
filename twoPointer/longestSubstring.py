# Longest Substring Without Duplicates
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        newSet = set()
        l = 0

        for r in range(len(s)):
            while s[r] in newSet:
                newSet.remove(s[l])
                l += 1 
            newSet.add(s[r])
            longest = max(longest, len(newSet))
        return longest 