# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,res = [(root, False)],[]
        while stack:
            node, f = stack.pop()
            if node:
                if f:
                    res.append(node.val)
                else:
                    stack.append((node.right,False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
