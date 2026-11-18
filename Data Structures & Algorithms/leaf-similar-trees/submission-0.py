# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1=[]
        tree2=[]
        ans=[]
        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if node.left is None and node.right is None:
                ans.append(node.val)
            
        dfs(root1)
        tree1=ans
        ans=[]
        dfs(root2)
        tree2=ans
        return tree1==tree2