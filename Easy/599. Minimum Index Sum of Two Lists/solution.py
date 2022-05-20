# My solution

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        flag = 0
        soi = len(list1) + len(list2)
        out = []
        for i,j in enumerate(list1):
            for x,y in enumerate(list2):
                if j == y:
                    if i+x <= soi:
                        soi = i+x
                        out.append([y,soi])
                        minn = soi
        out = [i[0] for i in out if i[1] == minn]
        return out
        
      
# Optimized

def findRestaurant(self, list1, list2):
    map2 = {x: i for i, x in enumerate(list2)}
    res, min_sum = [], float('inf')
    for i, rest in enumerate(list1):
        # optimize 
        if i > min_sum: 
            break
        if rest in map2:
            if i+map2[rest] < min_sum:
                res = [rest]
                min_sum = i+map2[rest]
            elif i+map2[rest] == min_sum:
                res += [rest]
    return res
