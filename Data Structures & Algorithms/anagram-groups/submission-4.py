class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            sort="".join(sorted(i))
            if(sort in dic.keys()):
                dic[sort].append(i)
            else:
                dic[sort]=[i]
        return list(dic.values())
            
        