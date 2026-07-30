# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None :
            return root==subRoot
        def issametree(a,b):
            if a is None or b is None:
                return a==b
            if a.val!=b.val:
                return False
            else:
                return issametree(a.left,b.left) and issametree(a.right,b.right)
        if issametree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or
            self.isSubtree(root.right,subRoot))
        