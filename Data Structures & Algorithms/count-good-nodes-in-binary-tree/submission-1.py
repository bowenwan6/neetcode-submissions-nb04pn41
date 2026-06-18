# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largestNow):
            if not node:
                return 0
            shouldAdd = 1 if node.val >= largestNow else 0
            largestNow = max(node.val, largestNow)
            return shouldAdd + dfs(node.left, largestNow) + dfs(node.right, largestNow)
        return dfs(root, root.val)