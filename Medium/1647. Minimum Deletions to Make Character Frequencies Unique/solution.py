class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0]*26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        freq.sort(reverse = 1)
        
        counter = 0
        max_freq = len(s)
        for f in freq:
            if f > max_freq:
                counter += f - max_freq
                f = max_freq
            max_freq = max(0,f-1)
        
        return counter
