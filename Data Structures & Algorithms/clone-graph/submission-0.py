"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None :
            return None
        otn={node:Node(node.val)}
        queue=deque([node])
        while queue:
            cur=queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in otn:
                    otn[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                otn[cur].neighbors.append(otn[neighbor])
        return otn[node]