class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        res=0
        while left<right:
            if height[left]==0:
                left+=1
            elif height[right]==0:
                right-=1
            elif height[left]!=0 and height[right]!=0:
                break
        while left<right:
            curr=0
            if height[left]<height[right]:
                indice=1
                while height[left+indice]<height[left]:
                    res+=height[left]-height[left+indice]
                    indice+=1
                left+=indice
            else:
                indice=1
                while height[right-indice]<height[right]:
                    res+=height[right]-height[right-indice]
                    indice+=1
                right-=indice
        return res

    



                
        
        