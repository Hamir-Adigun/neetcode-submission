class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        i,j=0,2%n
        while nums[i]!=nums[j]:
            i=(i+1)%n
            j=(j+2)%n
            if i==j:
                j+=1
        return nums[j]
        