# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        while head:
            a=head
            b=head
            while b.next and b.next.val!=-1:
                b=b.next
            if a.val!=b.val:
                return False
            b.val=-1
            head=a.next
        return not head

