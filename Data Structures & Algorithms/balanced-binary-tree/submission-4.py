# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True
        def height(a):
            if a is None:
                return 0
            left = height(a.left)
            if left == -1:
                return -1
            right = height(a.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            return  j 
        return height(root) != -1