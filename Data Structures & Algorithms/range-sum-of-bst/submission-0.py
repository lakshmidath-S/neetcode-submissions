# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum=0
        def dfs(node):
            nonlocal sum
            if not node:
                return 
            if low<=node.val<=high:
                sum+=node.val
            if node.left is  None and node.right is None:
                return 
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            return
        dfs(root)
        return sum
