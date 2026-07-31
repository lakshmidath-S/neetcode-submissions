# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=l1
        b=l2
        carry=0
        prev=None
        while a and b:
            sum=a.val+b.val+carry
            if sum>9:
                carry=1
                a.val=sum-10
            else:
                a.val=sum
                carry=0
            prev=a
            a=a.next
            b=b.next
        while a:
            if carry==1:
                sum=a.val+1
                if sum==10:
                    a.val=0
                else:
                    a.val=sum
                    carry=0
            prev=a
            a=a.next
        while b:
            new=ListNode()
            new.val=1
            new.next=None
            if carry==1:
                sum=b.val+1
                if sum==10:
                    new.val=0
                else:
                    new.val=sum
                    carry=0
            else:
                new.val=b.val
            prev.next=new
            prev=prev.next
            b=b.next
        if carry==1:
            new=ListNode()
            new.val=1
            new.next=None
            prev.next=new
        return l1

            
