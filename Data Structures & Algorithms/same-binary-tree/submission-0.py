# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node,stack):
            if node is None:
                stack.append(None)
                return 0
            else :
                stack.append(node.val)
                a=dfs(node.left,stack)
                b=dfs(node.right,stack)
                return 0

        stack1=[]
        stack2=[]
        dfs(p,stack1)
        dfs(q,stack2)
        return stack1==stack2