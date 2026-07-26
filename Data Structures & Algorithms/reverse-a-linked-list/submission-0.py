# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        a=head
        while a is not None:
            stack.append(a.val)
            a=a.next
        a=head
        while a is not None:
            a.val=stack.pop()
            a=a.next
        return head