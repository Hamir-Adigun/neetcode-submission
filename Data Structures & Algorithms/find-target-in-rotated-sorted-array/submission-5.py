class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(self,nums,target,l,r):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return mid
            r= -1 if nums[r]!=target else r
            return r
        if nums[0]<nums[len(nums)-1]:
            return binary(self,nums,target,0,len(nums)-1)
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=nums[r]:
                l=mid+1
            else:
               r=mid
        return max(binary(self,nums,target,r,len(nums)-1),binary(self,nums,target,0,r))

