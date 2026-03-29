class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p=0
        for i in range(len(nums)):
            b=target-nums[i] 
            num=nums[i+1:]
            if b in num :
                return [i,i+1+num.index(b)]
        return []

        