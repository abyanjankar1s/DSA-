# Binary Tree Right Side View
# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:Input: root = [1,2,3]

# Output: [1,3]
# Example 2:

# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,7]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 
        q = deque([root]) 

        while q:
            rightside = None 
            for i in range(len(q)):
                node = q.popleft() 
                if node:
                    rightside = node 
                    q.append(node.left) 
                    q.append(node.right) 
            if rightside:
                res.append(rightside.val) 
        return res 