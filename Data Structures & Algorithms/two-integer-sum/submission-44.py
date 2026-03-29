class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map={}
        for i,val in enumerate(nums):
            Map[val]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if(diff in Map and Map[diff]!=i):
                return [i,Map[diff]]