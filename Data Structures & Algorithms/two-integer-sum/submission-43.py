class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2= []
        for i, num in enumerate(nums):
            num2.append([num, i])

        num2.sort()

        l=0
        r=len(nums)-1
        while(l<r):
            somme=num2[l][0]+num2[r][0]
            if(somme<target):
                l+=1
            elif(somme>target):
                r-=1
            else:
                return [min(num2[l][1],num2[r][1]),max(num2[l][1],num2[r][1])]
        return []

        