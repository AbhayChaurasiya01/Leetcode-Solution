class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create difference matrix
        diff = [[0]* (n+1) for _ in range(n+1)]

        # Apply difference updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1

        # Prefix sum row-wise
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c-1]

        # Prefix sum column-wise
        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r-1][c]

        # Trim matrix to n x n
        res = [row[:n] for row in diff[:n]]
        return res
