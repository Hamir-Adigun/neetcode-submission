class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        for i in range(len(s1)):
            dic1[s1[i]]=1+ dic1.get(s1[i],0)
        l=0
        dic2={}
        for r in range(len(s2)):
            if s2[r] not in dic1:
                l=r+1
                dic2={}
            else:
                dic2[s2[r]]=1+ dic2.get(s2[r],0)
            if r-l+1>=len(s1):
                if dic1==dic2:
                    return True
                else:
                    if s2[l] in dic2:
                        dic2[s2[l]]-=1
                    l+=1
        return dic1==dic2
            