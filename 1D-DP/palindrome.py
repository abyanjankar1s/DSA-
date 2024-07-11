# Palindromic Substrings
# Solved 
# Given a string s, return the number of substrings within s that are palindromes.

# A palindrome is a string that reads the same forward and backward.

# Example 1:

# Input: s = "abc"

# Output: 3 

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 
        for i in range(len(s)):
            l = r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 
                l -= 1 
                r += 1 
            l = i 
            r = i+1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1 
                l -= 1 
                r += 1 
        return res 