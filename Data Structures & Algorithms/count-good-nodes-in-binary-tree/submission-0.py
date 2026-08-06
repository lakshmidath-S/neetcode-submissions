# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,count):
            if root is None :
                return 0
            if root.val>=count:
                count=max(count,root.val)
                good=1
            else:
                good=0
            return good +dfs(root.left,count)+dfs(root.right,count)
        return dfs(root,root.val)