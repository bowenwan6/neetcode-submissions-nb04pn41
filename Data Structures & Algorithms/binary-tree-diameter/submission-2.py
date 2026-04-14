# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        def dfs(x):
            nonlocal maxD
            if not x:
                return 0
            left_d = dfs(x.left)
            right_d = dfs(x.right)
            maxD = max(maxD, left_d + right_d)
            return 1 + max(left_d, right_d)
        dfs(root)
        return maxD
