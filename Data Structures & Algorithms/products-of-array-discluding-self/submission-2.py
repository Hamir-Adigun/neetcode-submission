class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic={}
        res=[0]*len(nums)
        for i in range(len(nums)):
            dic[nums[i]]=dic.get(nums[i],0)+1
        if dic.get(0,0)>=2:
            return res
        if dic.get(0,0)==1:
            p=1
            q=0
            for i in range(len(nums)):
                if nums[i]==0:
                    q=i
                    continue
                p=p*nums[i]
            res[q]=p
            return res
        p=1
        for i in range(len(nums)):
            p=p*nums[i]
        for i in range(len(nums)):
            res[i]=p//nums[i]
        return res

                    