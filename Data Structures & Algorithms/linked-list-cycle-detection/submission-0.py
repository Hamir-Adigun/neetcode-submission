# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        tortule=head
        lievre=head.next.next
        while tortule and lievre and lievre.next:
            if tortule==lievre:
                return True
            tortule=tortule.next
            lievre=lievre.next.next
        return False
        