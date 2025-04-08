# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverseLeafs(node):
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    reverseLeafs(node.left)
                if node.right:
                    reverseLeafs(node.right)

        reverseLeafs(root)
        return root