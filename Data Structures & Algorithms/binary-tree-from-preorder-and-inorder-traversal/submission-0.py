# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={}
        for i in range(len(inorder)):
            index[inorder[i]]=i
        def build(inos,inoe,pres,pree):
            if inos==inoe:
                return None
            root_val=preorder[pres]
            root=TreeNode(root_val)
            root_index=index[root_val]
            root.left=build(inos,root_index,pres+1,pres+1+(root_index-inos))
            root.right=build(root_index+1,inoe,pres+1+(root_index-inos),pree)
            return root
        return build(0,len(inorder),0,len(preorder))
       
