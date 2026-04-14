# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def listMaker(x, nodeList):
            if not x:
                nodeList.append(None)
                return
            nodeList.append(x.val)
            listMaker(x.left, nodeList)
            listMaker(x.right, nodeList)

        listP = []
        listMaker(p, listP)
        listQ = []
        listMaker(q, listQ)

        return listP == listQ