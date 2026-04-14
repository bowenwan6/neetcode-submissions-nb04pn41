# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def dfs(x, currD):
            if not x:
                return 0
            left_depth = dfs(x.left, currD)
            right_depth = dfs(x.right, currD)
            currD = left_depth + right_depth
            self.maxD = max(self.maxD, currD)
            return 1 + max(left_depth, right_depth)
        dfs(root, 0) # 0 is not important, it can be any number because currD will be reassigned
        return self.maxD