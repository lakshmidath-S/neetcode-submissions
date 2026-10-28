# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,sum):
            if not node:
                return False
            if node.left is None and node.right is None :
                return sum+node.val==targetSum
            if node.left:
                if dfs(node.left,sum+node.val):
                    return True
            if node.right:
                if dfs(node.right,sum+node.val):
                    return True
            return False
        return dfs(root,0)
            