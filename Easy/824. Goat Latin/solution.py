class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ac = 1
        v = 'aeiouAEIOU'
        k = sentence.split()
        for i in range(len(k)):
            if k[i][0] in v:
                k[i] = k[i] + 'ma' + 'a'*ac
            else:
                k[i] = k[i][1:] + k[i][0] + 'ma' + 'a'*ac
            ac += 1
        return ' '.join(k)
                
