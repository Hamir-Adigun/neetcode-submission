class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(t)):
                a=s[i]
                if not a in t or s.count(a)!=t.count(a):
                    return False
            return True
        