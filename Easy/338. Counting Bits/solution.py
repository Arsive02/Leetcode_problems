class Solution:
    def countBits(self, n: int) -> List[int]:
        for i in range(n+1):
            yield bin(i)[2:].count('1')
