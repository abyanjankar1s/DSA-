# Combination Target Sum II
# You are given an array of integers nums, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# Each element from nums may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:

# Input: candidates = [9,2,2,4,6,1,5], target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ] 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        candidates.sort() 

        def backtrack(curr, pos, target):
            if target == 0:
                res.append(curr[::])
            if target <= 0:
                return 
            prev = -1 
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i+1, target-candidates[i]) 
                curr.pop() 
                prev = candidates[i]
        backtrack([], 0, target) 
        return res 