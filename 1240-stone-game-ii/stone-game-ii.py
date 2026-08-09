from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        # Memoization
        dp = {}

        def dfs(i, M):
            if i == n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                opponent = dfs(i + X, max(M, X))
                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return dfs(0, 1)