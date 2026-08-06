# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=[]
        def preorder(root):
            if root is None:
                return 
            preorder(root.left)
            a.append(root.val)
            preorder(root.right)
            return
        preorder(root)
        return a[k-1]
