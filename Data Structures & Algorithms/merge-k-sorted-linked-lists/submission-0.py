# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=None
        head=None
        heap=[]
        for i in range(len(lists)):
            node=lists[i]
            if node:
                heapq.heappush(heap,(node.val,id(node),node))
                if node.next :
                    node=node.next
            else:
                continue
        while heap:
            b,c,a=heapq.heappop(heap)
            if a.next:
                heapq.heappush(heap,(a.next.val,id(a.next),a.next))
            if ans is None:
                ans=a
                ans.next=None
                head=ans
            else:
                ans.next=a
                ans=a
        return head
