# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast slow approach
        # find middle
        # reverse second half
        # merge
        if head is None or head.next is None:
            return 
        fast=head
        mid=head
        while fast.next and fast.next.next:
            mid=mid.next
            fast=fast.next.next
        second=mid.next
        mid.next=None
        fast=second
        prev=None
        while fast:
            a=fast.next
            fast.next=prev
            prev=fast
            fast=a
        first=head
        second=prev
        while second:
            temp=first.next
            first.next=second
            temp2=second.next
            second.next=temp
            first=temp
            second=temp2
