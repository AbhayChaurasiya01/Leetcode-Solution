# 3234. Count the Number of Substrings With Dominant Ones
# LeetCode Python Solution

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        # zero + zero^2 must be <= n
        z = 0
        while z + z * z <= n:
            last_invalid = -1
            count0 = 0
            count1 = 0
            l = 0

            for r in range(n):
                if s[r] == '0':
                    count0 += 1
                else:
                    count1 += 1

                # shrink window
                while l < r:
                    if s[l] == '0' and count0 > z:
                        count0 -= 1
                        last_invalid = l
                        l += 1
                    elif s[l] == '1' and count1 - 1 >= z * z:
                        count1 -= 1
                        l += 1
                    else:
                        break

                # if valid: exactly z zeros and >= z^2 ones
                if count0 == z and count1 >= z * z:
                    ans += (l - last_invalid)

            z += 1

        return ans
