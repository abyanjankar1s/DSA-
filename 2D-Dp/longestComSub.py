# Longest Common Subsequence
# Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# A common subsequence of two strings is a subsequence that exists in both strings.

# Example 1:

# Input: text1 = "cat", text2 = "crabt" 

# Output: 3  

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)] 

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) 

        return dp[0][0] 