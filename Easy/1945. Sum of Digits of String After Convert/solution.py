class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = {y:str(x+1) for x,y in enumerate(string.ascii_lowercase)}
        t = ''
        for i in s:
            t += l[i]
        i = 0
        while i < k:
            t = str(sum(list(map(int,list(t)))))
            i += 1
        return t
