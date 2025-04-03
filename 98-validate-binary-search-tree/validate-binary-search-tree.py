# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def aux(self, root, lowest, highest):
        if root.val <= lowest or root.val >= highest:
            return False
            
        left_valid = self.aux(root.left, lowest, min(highest, root.val)) if root.left else True
        right_valid = self.aux(root.right, max(lowest, root.val), highest) if root.right else True
        
        return left_valid and right_valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lowest = -float('inf')
        highest = float('inf')
        return self.aux(root, lowest, highest)
    