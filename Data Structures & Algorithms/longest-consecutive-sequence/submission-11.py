class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dic={}
        for i in nums:
            dic[i]=[i,i]
        for i in dic:
            if i+1 not in dic and i-1 not in dic:
                dic[i]=-1
        for i in dic:
            if dic[i]==-1:
                continue
            p=i+1
            b=i-1
            while p in dic and dic[p]!=-1:
                dic[i][1]=p
                dic[p]=-1
                p=p+1
            while b in dic and dic[b]!=-1:
                dic[i][0]=b
                dic[b]=-1
                b=b-1
        k=1
        for i in dic:
            if dic[i]==-1:
                continue
            c=dic[i][1]-dic[i][0]+1
            if c>k:
                k=c
        return k


        
        