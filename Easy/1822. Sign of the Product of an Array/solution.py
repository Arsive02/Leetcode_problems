class Solution:
    def arraySign(self, nums: List[int]) -> int:
        counter = 0
        for x in nums:
            if x < 0:
                counter += 1
            if x == 0:
                return 0
        if counter % 2:
            return -1
        return 1
      
 
