# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthAux(self, root: Optional[TreeNode], level: int):
        if not root:
            return level
        
        level += 1

        return max(self.maxDepthAux(root.left, level), self.maxDepthAux(root.right, level))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthAux(root, 0)