# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ga=float('-inf')
        def helper(a):
            nonlocal ga
            if a is None:
                return 0
            left=helper(a.left)
            right=helper(a.right)
            ga=max(ga,a.val+max(left,0)+max(right,0))
            return a.val+max(left,right,0)
        helper(root)
        return ga
        