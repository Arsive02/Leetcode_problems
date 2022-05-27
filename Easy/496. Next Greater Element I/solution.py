class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            k = nums2.index(i)
            t = -1
            for j in range(k+1,len(nums2)):
                if nums2[j] > nums2[k]:
                    t = nums2[j]                
                    break
            l.append(t)
        return l
            
