class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = 0
        st = -1
        for i,j in enumerate(nums):
            if j == 1:
                st = i
                break
        if st == -1:
            return True
        
        nums = nums[st:]
        for i in range(1, len(nums)):
            if nums[i] == 1:
                if counter < k:
                    return False
                counter = 0
            else:
                counter += 1
        return True
            
