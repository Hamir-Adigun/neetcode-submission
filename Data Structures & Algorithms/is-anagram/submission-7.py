class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dic_1={}
        dic_2={}
        for i in range(len(s)):
            dic_1[s[i]] = dic_1.get(s[i], 0) + 1
            dic_2[t[i]] = dic_2.get(t[i], 0) + 1
        return (dic_1==dic_2)
        