class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes=[1]*len(nums)
        suffixes=[1]*len(nums)
        res=[]
        for i in range(1,len(nums)):
            prefixes[i]=prefixes[i-1]*nums[i-1]
        for i in range(1,len(nums)):
            suffixes[len(nums)-1-i]=suffixes[len(nums)-i]*nums[len(nums)-i]
        for i in range(len(nums)):
            res.append(prefixes[i]*suffixes[i])
        return res
