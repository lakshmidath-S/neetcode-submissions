# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        if head.next is not None:
            stack=[]
            a=head
            n=0
            while a is not None:
                a=a.next
                n+=1
            a=head
            i=0
            while a is not None:
                b=a
                a=a.next
                if i==(n-1)//2:
                    b.next=None
                if i>(n-1)//2:
                    b.next=None
                    stack.append(b)
                i+=1
            a=head
            i=0
            while a is not None:
                if (i)%2==0 and stack:
                    b=stack.pop()
                    c=a.next
                    a.next=b
                    b.next=c
                    a=c
                    i+=2
                else:
                    i+=1
                    a=a.next