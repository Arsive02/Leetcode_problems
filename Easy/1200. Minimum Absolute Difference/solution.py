class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        k = []
        arr.sort()
        minn = arr[-1]
        for i in range(len(arr)-1):
            t = abs(arr[i]-arr[i+1])
            if t < minn:
                minn = t
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) == minn:
                k.append([arr[i],arr[i+1]])
        return k
                    
