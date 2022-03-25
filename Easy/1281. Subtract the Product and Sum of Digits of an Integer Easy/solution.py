class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        r = 1
        for i in str(n):
            r *= int(i)
        s = sum(list(map(int,list(str(n)))))
        return r-s
