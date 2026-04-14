# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(x, y):
            if not x and not y:
                return True
            
            if x and y and x.val == y.val:
                return sameTree(x.left, y.left) and sameTree(x.right, y.right)
            
            return False

        def subtree(x, y):
            if not y:
                return True
            if not x:
                return False
            if sameTree(x,y):
                return True
            return (subtree(x.left, y)
            or subtree(x.right, y))

        return subtree(root, subRoot)

            
        