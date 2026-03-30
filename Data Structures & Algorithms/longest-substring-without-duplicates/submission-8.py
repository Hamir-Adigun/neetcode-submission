class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return n
        l=r=0
        i=0
        p=0
        dic={}
        while r<n:
            while r<n:
                if s[r] not in dic:   
                    dic[s[r]]=r
                    p+=1
                    r+=1
                else:
                    if dic[s[r]]<l:
                        dic[s[r]]=r
                        p+=1
                        r+=1
                    else:
                        break
            if r<n:
                l=dic[s[r]]+1
                i=max(i,p)
                p=r-l
            else:
                i=max(i,p)
        return i