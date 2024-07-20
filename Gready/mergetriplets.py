# Merge Triplets to Form Target
# You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

# To obtain target, you may apply the following operation on triplets zero or more times:

# Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# * E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

# Return true if it is possible to obtain target as an element of triplets, or false otherwise.

# Example 1:

# Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]

# Output: true 

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        