class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for x in range(len(arr)):
            for y in range(x+1,len(arr)+1):
                t = arr[x:y]
                if len(t)%2:
                    s += sum(t)
        return s
