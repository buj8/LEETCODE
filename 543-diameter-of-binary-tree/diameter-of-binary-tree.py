# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            nonlocal diameter
            
            # Calculate heights of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter if path through current node is longer
            diameter = max(diameter, left_height + right_height)
            
            # Return height of current subtree
            return max(left_height, right_height) + 1
        
        height(root)
        return diameter