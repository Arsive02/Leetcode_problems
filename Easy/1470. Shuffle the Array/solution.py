class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a,b = nums[:n],nums[n:]
        k = []
        ac,bc = 0, 0
        for i in range(2*n):
            if not i%2:
                k.append(a[ac])
                ac += 1
            else:
                k.append(b[bc])
                bc += 1
        return k
