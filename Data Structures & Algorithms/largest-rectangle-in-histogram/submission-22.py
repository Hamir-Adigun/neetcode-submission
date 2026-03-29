class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        for i in range(0,len(heights)):
            if len(stack)==0:
                stack.append((i,heights[i],i))
            elif stack[-1][1]<= heights[i]:
                stack.append((i,heights[i],i))
            else:
                extendback=0
                while len(stack)>0 and stack[-1][1]>heights[i] :
                    a=stack.pop()
                    extendback=a[0]
                    res=a[1]*(i-a[0]) if res<a[1]*(i-a[0]) else res 
                stack.append((extendback,heights[i],i))
        while len(stack)>0:
            b=stack.pop()
            res=b[1]*(len(heights)-b[0]) if res<b[1]*(len(heights)-b[0]) else res
        return res
            

