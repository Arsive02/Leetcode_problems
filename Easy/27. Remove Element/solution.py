class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ele = 0
        for i in nums:
            if i != val:
                nums[ele] = i
                ele += 1
        return ele
