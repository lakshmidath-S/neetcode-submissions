# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameter=0
        def height(a):
            if a is None:
                return 0
            nonlocal diameter
            left=height(a.left)
            right=height(a.right)
            diameter=max(diameter,left+right)
            return 1+max(left,right)
        height(root)
        return diameter