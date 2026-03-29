# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        val=1000
        p=0
        t=0
        for i in range(len(lists)):
            if not lists[i]:
                t+=1
                continue
            val,p= (lists[i].val,i) if lists[i].val<=val else (val,p)
        if t==len(lists):
            return None
        start=ListNode(val,None)
        lists[p]=lists[p].next if lists[p] else None
        start.next=self.mergeKLists(lists)
        return start
