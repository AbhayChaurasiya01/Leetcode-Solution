class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]    # from left
                elif j == 0:
                    grid[i][j] += grid[i-1][j]    # from top
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]
