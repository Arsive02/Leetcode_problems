class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        can = nums[0]
        for i in range(len(nums)):
            if nums[i] == can:
                count += 1
            else:
                count -= 1
                if count == 0:
                    can = nums[i]
                    count = 1
        return can
