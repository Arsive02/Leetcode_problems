class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = Counter((s1 + ' ' + s2).split())
        for i,j in d.items():
            if j == 1:
                yield i
        
