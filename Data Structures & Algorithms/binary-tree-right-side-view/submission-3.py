# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root,level):
            if root is None:
                return 
            dfs(root.left,level+1)
            levels[level]=root.val
            dfs(root.right,level+1)
            return
        if root is None:
            return []
        levels={}
        dfs(root,0)
        return [levels[i] for i in range(len(levels))]
        