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
        def search(current_layer_nodes):
            next_layer_nodes = []
            layer_values = []
            for node in current_layer_nodes:
                layer_values.append(node.val)
                if node.left:
                    next_layer_nodes.append(node.left)
                if node.right:
                    next_layer_nodes.append(node.right)
            
            res.append(layer_values)
            return next_layer_nodes
        current_layer = [root]
        while current_layer:
            current_layer = search(current_layer)
        return res