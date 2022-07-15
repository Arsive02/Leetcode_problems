class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        for a, row in enumerate(grid):
            for b, val in enumerate(row):
                if val and (a, b) not in seen:
                    shape = 0
                    stack = [(a, b)]
                    seen.add((a,b))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= x < len(grid) and 0 <= y < len(grid[0])
                                    and grid[x][y] and (x, y) not in seen):
                                stack.append((x, y))
                                seen.add((x, y))
                    ans = max(ans, shape)
        return ans
