class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        d = dict()
        for i in arr1:
            d[i] = d.get(i,0)+1
        k = [i for i in arr1 if i not in arr2]
        c = 0
        for i in arr2:
            for j in range(d[i]):
                arr1[c] = i
                c += 1
        arr1[c:] = k
        return arr1
