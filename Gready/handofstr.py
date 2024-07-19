# Hand of Straights
# You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

# You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

# Return true if it's possible to rearrange the cards in this way, otherwise, return false.

# Example 1:

# Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

# Output: true 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        