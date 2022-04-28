class Solution:
    def isHappy(self, n: int) -> bool:
        l = set()
        if n == 1:
            return True
        while 1:
            k = sum([int(i)**2 for i in str(n)])
            if k == 1:
                return True
            if k in l:
                return False
            l.add(k)
            n = k
