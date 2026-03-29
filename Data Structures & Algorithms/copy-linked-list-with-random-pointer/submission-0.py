
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dic={}
        if not head:
            return None
        start=head
        while start:
            inter=Node(start.val)
            dic[start]=inter
            start=start.next
        start=head
        while start:
            dic[start].next=dic[start.next] if start.next else None
            dic[start].random=dic[start.random] if start.random else None
            start=start.next
        return dic[head]


        