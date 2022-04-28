class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        counter = 0
        t = ''
        tt = ''
        for i,j in enumerate(s1):
            k = s2.find(j)
            if k == -1:
                return False
            if j != s2[i]:
                counter += 1
                t += j
                tt += s2[i]
            if counter > 2:
                return False
        if counter == 2:
            if t[0] != tt[1] or t[1] != tt[0]:
                return False
            return True
        return False
