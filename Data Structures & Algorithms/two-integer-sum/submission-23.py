class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            b=target-nums[i]
            if b in nums[i+1:len(nums)]:
                if nums.count(b)==1:
                    return [i,nums.index(b)]
                else:
                    nums1=nums[i+1:len(nums)]
                    if i==0:
                        return [i,nums1.index(b)+1]
                    else:
                        return[i,nums1.index(b)+i+1]

        return "Cette liste ne contient pas de couples solutions"
