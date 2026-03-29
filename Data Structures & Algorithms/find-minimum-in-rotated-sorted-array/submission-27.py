class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        if nums[l]<=nums[r]:
            return nums[l]
        mid=0
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=nums[r]:
                l=mid+1 ## se rapproche petit à petit de r
            else:
                r=mid ## car le minimum peut être en mid
        return nums[r]