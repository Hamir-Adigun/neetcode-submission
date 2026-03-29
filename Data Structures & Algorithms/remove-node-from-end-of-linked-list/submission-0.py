# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz=0
        start=head
        while start:
            sz+=1
            start=start.next
        p=sz-n
        def remove(hea: Optional[ListNode],p:int)->Optional[ListNode]:
            if p==0:
                hea=hea.next
                return hea
            if not hea:
                return None
            hea.next=remove(hea.next,p-1)
            return hea
        head=remove(head,p)
        return head