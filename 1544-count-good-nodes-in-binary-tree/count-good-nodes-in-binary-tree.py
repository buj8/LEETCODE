# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0

        def dfs(root, curmax):
            if root: 
                if root.val >= curmax:
                    curmax = root.val
                    nonlocal good_count
                    good_count += 1
                dfs(root.left, curmax)
                dfs(root.right, curmax)

        dfs(root, root.val)
        return good_count