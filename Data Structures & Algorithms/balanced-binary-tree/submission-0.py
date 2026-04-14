# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        def dfs(x):
            if not x:
                return 0
            left = dfs(x.left)
            right = dfs(x.right)
            self.res = max(self.res, abs(left - right))
            return 1 + max(left, right)
        dfs(root)
        return self.res < 2
            
            

        