from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        k = Counter('balloon')
        counter = 0
        f = 0
        while not f:
            for x,y in k.items():
                if d[x] - y < 0:
                    f = 1
                    break
                d[x] = d[x] - y
            if not f:
                counter += 1
        return counter
        
# ALTERNATE SOLUTION
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))
