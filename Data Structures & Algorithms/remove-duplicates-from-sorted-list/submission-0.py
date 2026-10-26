# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        val=float("-inf")
        a=ListNode(None)
        a.next=head
        prev=a
        curr=head
        while curr:
            if curr.val<=val:
                prev.next=curr.next
            else:
                val=curr.val
                prev=curr
            curr=curr.next
        return a.next
