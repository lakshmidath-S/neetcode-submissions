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
            return(1+max(height(a.left),height(a.right))) 
        return abs(height(root.left)-height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)