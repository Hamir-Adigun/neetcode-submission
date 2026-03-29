# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
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
        #reorderaux(head)
        #return None 
        """
        if not head or not head.next or not head.next.next:
            return None
        liste=[]
        curr=head
        prev=None
        while curr.next:
            prev=curr
            curr=curr.next
            prev.next=None
            liste.append(prev)
        liste.append(curr)
        l,r=0,len(liste)-1
        liste2=[]
        while l<r:
            liste[l].next=liste[r]
            liste2.append(liste[l])
            l+=1
            r-=1
        if l==r:
            liste2.append(liste[l])
        for i in range(len(liste2)-2):
            liste2[i].next.next=liste2[i+1]
        liste2[len(liste2)-2].next.next=liste2[len(liste2)-1]
        head=liste2[0]
        return None
        
            



            

            
        
        