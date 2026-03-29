class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen=[]
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r :
                d=nums[r]+nums[l]+nums[i]
                if d>0:
                    r=r-1
                elif d<0:
                    l=l+1
                else:
                    liste=[nums[i],nums[l],nums[r]]
                    if liste not in seen :
                        seen.append(liste)
                    l=l+1
        return seen


        