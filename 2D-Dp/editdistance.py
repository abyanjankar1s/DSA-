# Edit Distance
# You are given two strings word1 and word2, each consisting of lowercase English letters.

# You are allowed to perform three operations on word1 an unlimited number of times:

# Insert a character at any position
# Delete a character at any position
# Replace a character at any position
# Return the minimum number of operations to make word1 equal word2.

# Example 1:

# Input: word1 = "monkeys", word2 = "money"

# Output: 2 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)] 

        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j 
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i 
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1] 
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) 
        return dp[0][0] 