# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p is None) ^ (q is None):
            return False
        
        if p.val != q.val:
            return False
        
        right_same = self.isSameTree(p.right, q.right)
        left_same = self.isSameTree(p.left, q.left)
        
        result = right_same and left_same
        
        return result
 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        
        if self.isSameTree(root, subRoot):
            return True
            
        left_result = self.isSubtree(root.left, subRoot)
        
        if left_result:
            return True
            
        right_result = self.isSubtree(root.right, subRoot)
        
        if right_result:
            return True

        return False