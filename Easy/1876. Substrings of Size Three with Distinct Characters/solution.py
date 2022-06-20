class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-3+1):
            t = s[i:i+3]
            if len(set(t)) == 3:
                counter += 1
        return counter
