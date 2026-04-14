# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def dfs(x):
            if not x:
                return 0
            leftD = dfs(x.left)
            rightD = dfs(x.right)
            combinedD = leftD + rightD
            self.maxD = max(self.maxD, combinedD)
            return 1 + max(leftD, rightD)
        dfs(root)
        return self.maxD
