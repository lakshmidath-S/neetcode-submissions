# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inr(root,ans):
            if root.left :
                inr(root.left,ans)
            ans.append(root.val)
            if root.right:
                inr(root.right,ans)
        ans=[]
        if root:
            inr(root,ans)
            return ans
        return []
        
