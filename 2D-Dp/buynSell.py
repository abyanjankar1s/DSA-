# Buy and Sell Crypto with Cooldown
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may buy and sell one NeetCoin multiple times with the following restrictions:

# After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
# You may only own at most one NeetCoin at a time.
# You may complete as many transactions as you like.

# Return the maximum profit you can achieve.

# Example 1:

# Input: prices = [1,3,4,0,4]

# Output: 6 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} #key: (index, Buying) value: maxProfit 

        def dfs(i, buying):
            if i >= len(prices):
                return 0 
            if (i, buying) in dp:
                return dp[(i, buying)] 
            if buying:
                buy = dfs(i+1, not buying) - prices[i] 
                cooldown = dfs(i+1, buying) 
                dp[(i, buying)] = max(buy, cooldown) 
            else:
                sell = dfs(i+2, not buying) + prices[i]  #not buying because of negeation since its in Flase cuur we negate to true by not buying.
                cooldown = dfs(i+1, buying) 
                dp[(i, buying)] = max(sell, cooldown) 
            return dp[(i, buying)] 
        
        return dfs(0, True)