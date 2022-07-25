class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = dict()
        for i in arr:
            k = bin(i)[2:].count('1')
            d[k] = d.get(k, []) + [i]
        t = []
        keys = sorted(d.keys())
        for key in keys:
            t.extend(sorted(d[key]))
        return t
        
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num: (sum((num >> i) & 1 for i in range(32)), num))


                    
