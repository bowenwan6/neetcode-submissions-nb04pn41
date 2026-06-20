# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, NoDefault0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        fullL = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            fullL.append(node.val)
            dfs(node.right)
        dfs(root)
        return fullL[k-1]

