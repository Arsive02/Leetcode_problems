class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearchLeft(nums, target):
            l,r = 0,len(nums)-1
            while l <= r:
                m = (l+r)//2
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        def binSearchRight(nums, target):
            l,r = 0,len(nums)-1
            while l <= r:
                m = (l+r)//2
                if target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return r
        
        l,r = binSearchLeft(nums, target), binSearchRight(nums, target)
        return [l,r] if l <= r else [-1,-1]
            
        
                    
