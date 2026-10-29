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
            if node.val<low:
                dfs(node.right)
            elif node.val>high:
                dfs(node.left)
            else:
                sum+=node.val
                dfs(node.left)
                dfs(node.right)
            return
        dfs(root)
        return sum
