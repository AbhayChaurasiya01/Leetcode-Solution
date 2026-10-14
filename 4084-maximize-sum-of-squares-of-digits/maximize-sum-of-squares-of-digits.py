class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Step 1: the biggest possible digit sum is 9 * num
        if sum > 9 * num:
            return ""

        ans = []

        # Step 2: fill every position from left to right
        for _ in range(num):
            digit = min(9, sum)   # take as much as we can, at most 9
            ans.append(str(digit))
            sum -= digit

        return "".join(ans) if sum == 0 else ""