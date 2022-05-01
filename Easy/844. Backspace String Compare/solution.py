class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)
    
    def check(self, string):
            stack = []
            for i in string:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
