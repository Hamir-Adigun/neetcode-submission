# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorderaux(head)->Optional[ListNode]:
            if not head or not head.next or not head.next.next:
                return head
            curr=head
            prev=None
            while curr.next:
                prev=curr
                curr=curr.next
            prev.next=None
            suiv=head.next
            head.next=curr
            curr.next=reorderaux(suiv)
            return head
        reorderaux(head)
        return None
        
        