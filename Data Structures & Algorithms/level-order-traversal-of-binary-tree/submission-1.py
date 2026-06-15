# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        def search(layerNodes):
            nextLayerNode = []
            currLayerVal = []
            if layerNodes:
                for node in layerNodes:
                    currLayerVal.append(node.val)
                    if node.left:
                        nextLayerNode.append(node.left)
                    if node.right:
                        nextLayerNode.append(node.right)
            res.append(currLayerVal)
            return nextLayerNode
        curr = [root]
        while curr:
            curr = search(curr)
        return res
