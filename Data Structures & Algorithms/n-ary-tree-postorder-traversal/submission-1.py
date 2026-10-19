"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack=[]
        if root is None:
            return stack
        def po(root):
            value=root.val
            if root.children is None:
                return 
            for i in root.children:
                po(i)
            stack.append(value)
        po(root)
        return stack