class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = -1 
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not any(letter in words[i] for letter in words[j]):
                    if len(words[i]) * len(words[j]) > max_len:
                        max_len = len(words[i]) * len(words[j])
        if max_len == -1:
            return 0
        return max_len
                
