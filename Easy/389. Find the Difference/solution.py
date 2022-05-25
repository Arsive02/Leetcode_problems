from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for key in t.keys():
            if key not in s or s[key] != t[key]:
                return key
            
