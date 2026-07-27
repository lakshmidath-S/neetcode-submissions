# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        while head:
            if head in a:
                return True
            else:
                a.add(head)
                head=head.next
        return False