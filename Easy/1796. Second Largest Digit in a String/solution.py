class Solution:
    def secondHighest(self, s: str) -> int:
        t = list(set(int(i) for i in s if i.isdigit()))
        if not t or len(t) == 1:
            return -1
        k = max(t)
        t.pop(t.index(k))
        return max(t)
