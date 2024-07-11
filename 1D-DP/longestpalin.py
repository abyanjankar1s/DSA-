# Longest Palindromic Substring
# Given a string s, return the longest substring of s that is a palindrome.

# A palindrome is a string that reads the same forward and backward.

# If there are multiple palindromic substrings that have the same length, return any one of them.

# Example 1:

# Input: s = "ababd"

# Output: "bab" 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        resL = 0 

        for i in range(len(s)):
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resL:
                    res = s[l:r+1] 
                    resL = r-l+1

                l -= 1
                r += 1
            
            l, r = i, i+1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resL:
                    res = s[l:r+1] 
                    resL = r-l+1
                l -= 1
                r += 1 
        return res 