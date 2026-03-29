# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        somme=ListNode()
        curr=somme
        s1=l1
        s2=l2
        v3=0
        prev=None
        while s1 or s2:
            v1=s1.val if s1 else 0
            v2=s2.val if s2 else 0
            v3,v=(1,v1+v2+curr.val-10) if curr.val+v1+v2>=10 else (0,v1+v2+curr.val)
            curr.val=v
            prev=curr
            curr.next=ListNode(v3)
            curr=curr.next
            s1=s1.next if s1 else None
            s2=s2.next if s2 else None
        if curr.val==0:
            prev.next=None
        return somme
     
        