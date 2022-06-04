class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        e_pos = [i for i,j in enumerate(s) if j == c]
        for i,j in enumerate(s):
            m = len(s)
            for x in e_pos:
                if x - i < m:
                    m = abs(x-i)
            answer.append(m)
        return answer
        
