class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(nums:List[int],target:int,l,r)->int:
            while l<=r:
                mean=(l+r)//2
                if nums[mean]<target:
                    l=mean+1
                elif nums[mean]>target:
                    r=mean-1
                else:
                    return mean
            return -1
        i=0
        while 2**i<len(nums) and nums[2**i]<target:
            i+=1
        if 2**i>=len(nums):
            return binarysearch(nums,target,(2**i)//2,len(nums)-1)
        else:
            return binarysearch(nums,target,(2**i)//2,2**i)



        