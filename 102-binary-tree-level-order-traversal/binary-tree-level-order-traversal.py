# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = defaultdict(list)
        self.aux(root, arr, 0)
        return list(arr.values())
    
    def aux(self, root, arr, level):
        if root:
            arr[level].append(root.val)
            self.aux(root.left, arr, level+1)
            self.aux(root.right, arr, level+1)
        