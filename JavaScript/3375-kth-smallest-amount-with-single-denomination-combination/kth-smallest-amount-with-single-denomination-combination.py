class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        from functools import reduce

        n = len(coins)

        def count(x):
            ans = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if valid:
                    if bits % 2:
                        ans += x // lcm
                    else:
                        ans -= x // lcm

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left