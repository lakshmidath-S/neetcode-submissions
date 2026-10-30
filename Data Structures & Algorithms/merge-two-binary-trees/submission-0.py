# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        a=root1
        b=root2
        a.val+=b.val
        a.left = self.mergeTrees(a.left, b.left)
        a.right = self.mergeTrees(a.right, b.right)
        return root1

            