class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        counter = 0
        f = 0
        m = 1e5
        for k,i in enumerate(points):
            if i[0] == x or i[1] == y:
                f = 1
                dist = abs(x-i[0]) + abs(y-i[1])
                if dist < m:
                    m = dist
                    result = k
        if not f:   
            return -1
        return result
