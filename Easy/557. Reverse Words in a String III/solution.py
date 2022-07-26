class Solution:
    def reverseWords(self, s: str) -> str:
        k = []
        for i in s.split():
            k.append(i[::-1])
        return ' '.join(k)
        
