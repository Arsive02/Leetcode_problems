class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            if all(1 if i%int(x) == 0 else 0 for x in str(i)):
                l.append(i)
        return l
            
