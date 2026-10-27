class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]   # start: all walls
        r = c = 0
        grid[0][0] = '.'

        # how far is (r, c) from the line start -> end?
        def dist(r, c):
            return abs(r * (n - 1) - c * (m - 1))

        while r < m - 1 or c < n - 1:
            # go down if right is impossible, or down is at least as close
            if r < m - 1 and (c == n - 1 or dist(r + 1, c) <= dist(r, c + 1)):
                r += 1
            else:
                c += 1
            grid[r][c] = '.'                     # carve the road

        return [''.join(row) for row in grid]