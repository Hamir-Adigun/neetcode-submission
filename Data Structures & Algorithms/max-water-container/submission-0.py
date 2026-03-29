class Solution:
    def maxArea(self, heights: List[int]) -> int:
        k=0
        l=0
        r=len(heights)-1
        while l<r:
            if heights[l]<heights[r]:
                k=max(k,(r-l)*heights[l])
                l=l+1
            else:
                k=max(k,(r-l)*heights[r])
                r=r-1
        return k
        
        