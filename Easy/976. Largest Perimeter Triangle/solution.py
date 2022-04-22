class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = 1)
        f = 1
        for i in range(0,len(nums)-2):
            if self.checkValidTriangle(nums[i:i+3]):
                return sum(nums[i:i+3])
        if f:
            return 0
    
    def checkValidTriangle(self, nums):
        a,b,c = nums
        if a < b+c and b < a+c and c < a+b:
            return 1
        return 0
