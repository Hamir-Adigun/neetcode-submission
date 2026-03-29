class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def Eatingall(self,piles:List[int],h:int,m:int)->bool:
            for i in piles:
                h-=i//m if i%m==0 else 1+ i//m
            if h<0:
                return False
            return True
        m=0
        for i in piles:
            m=i if m<i else m
        l,r=1,m
        res=m
        while l<=r:
            k=(l+r)//2
            if Eatingall(self,piles,h,k):
                res=k
                r=k-1
            else:
                l=k+1
        return res

