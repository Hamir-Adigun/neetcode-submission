class Solution(object):
    def hasDuplicate(self,nums):
        for i in range (len(nums)):
            a=nums[i]
            if nums.count(a)!=1:
                return True
        return False