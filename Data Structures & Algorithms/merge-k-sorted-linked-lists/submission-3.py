# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        def merge(left,right):
            if left is None:
                return right
            if right is None:
                return left
            a=left
            b=right
            head=ListNode()
            temp=head
            while a and b:
                if a.val<b.val:
                    temp.next=a
                    temp=temp.next
                    a=a.next
                else:
                    temp.next=b
                    temp=temp.next
                    b=b.next
            while a:
                temp.next=a
                temp=temp.next
                a=a.next
            while b:
                temp.next=b
                temp=temp.next
                b=b.next
            return head.next

            
            
        def mergesort(lists):
            n=len(lists)
            if n==1:
                return lists[0]
            mid=n//2
            left=mergesort(lists[:mid])
            right=mergesort(lists[mid:])
            return merge(left,right)
        return  mergesort(lists)