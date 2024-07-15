# Coin Change II
# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

# You may assume that you have an unlimited number of each coin and that each value in coins is unique.

# Example 1:

# Input: amount = 4, coins = [1,2,3]

# Output: 4 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1) 
        dp[0] = 1 

        for i in range(len(coins)-1,-1,-1):
            newDp = [0] * (amount+1) 
            newDp[0] = 1 
            for a in range(1, amount+1):
                newDp = dp
                if a - coins[i] >= 0:
                    newDp[a] += newDp[a-coins[i]] 
            dp = newDp 
            
        return dp[amount] 