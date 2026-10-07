# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inr(root):
            if not root :
                return
            inr(root.left)
            ans.append(root.val)
            inr(root.right)
        inr(root)
        return ans
        
