class Solution:
    def isHappy(self, n: int) -> bool:
        l = set()
        if n == 1:
            return True
        while 1:
            k = sum([int(i)**2 for i in str(n)])
            if k == 1:
                return True
            if k in l:
                return False
            l.add(k)
            n = k

            
# Approach 2:

class Solution:
    def isHappy(self, n: int) -> bool:
        def steps(n):
            res = 0 
            while n > 0 :
                res += (n % 10) ** 2
                n = n // 10 
            return res 
        
        slow, fast  = n, n
        while fast != 1 and steps(fast) != 1:
            slow = steps(slow)
            fast = steps(steps(fast))
            if slow == fast:
                return False 
        return True 
