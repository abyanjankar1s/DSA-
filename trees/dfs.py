# Level Order Traversal of Binary Tree
# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]

# Output: [[1],[2,3],[4,5,6,7]]
# Example 2:

# Input: root = [1]

# Output: [[1]]
# Example 3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] 
        q = deque() 

        if root:
            q.append(root)

        while q:
            val = [] 
            for i in range(len(q)):

                node = q.popleft() 
                val.append(node.val) 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right) 
            res.append(val)
        return res 







