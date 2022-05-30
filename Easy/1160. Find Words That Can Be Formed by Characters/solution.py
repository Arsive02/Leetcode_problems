from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        strlen = 0
        for x in words:
            k = Counter(x)
            f = 1
            g = 0
            for y,z in k.items():
                if z <= d[y]:
                    g += z
                else:
                    f = 0
            if f:
                strlen += g
        return strlen
