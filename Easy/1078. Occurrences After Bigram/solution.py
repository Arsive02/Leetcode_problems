class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        for i in range(2,len(text)):
            if text[i-2] == first and text[i-1] == second:
                yield text[i]
            
            
