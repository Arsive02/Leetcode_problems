class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i,j in enumerate(s):
            if d[j] == 1:
                return i
        return -1
