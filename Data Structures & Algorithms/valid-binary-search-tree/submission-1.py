# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low=float('-inf')
        high=float('inf')
        def isvalid(node,low,high):
            if node is None:
                return True
            if node.val<=low or node.val>=high:
                return False
            return isvalid(node.left,low,node.val) and isvalid(node.right,node.val,high)
        return isvalid(root,low,high)