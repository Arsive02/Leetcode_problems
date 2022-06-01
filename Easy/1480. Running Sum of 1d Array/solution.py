class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            output.append(s)
        return output
            
        
        
