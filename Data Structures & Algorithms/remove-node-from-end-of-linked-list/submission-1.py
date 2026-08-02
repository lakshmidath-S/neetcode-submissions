# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=head
        count=0
        temp=ListNode(None)
        while a :
            a=a.next
            count+=1
        if count == n:
            return head.next
        i=0
        prev=None
        a=head
        while a:
            if i==count-n:
                prev.next=a.next
                break
            else:
                prev=a
                a=a.next
                i+=1
        return head
        