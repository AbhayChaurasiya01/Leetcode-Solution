class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing_zeros = []

        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        for i in range(n):
            required = n - 1 - i

            j = i
            while j < n and trailing_zeros[j] < required:
                j += 1

            if j == n:
                return -1

            while j > i:
                trailing_zeros[j], trailing_zeros[j - 1] = (
                    trailing_zeros[j - 1],
                    trailing_zeros[j]
                )
                swaps += 1
                j -= 1

        return swaps