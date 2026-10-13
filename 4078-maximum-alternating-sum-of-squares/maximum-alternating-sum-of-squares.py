class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        neg = len(sq) // 2          # smallest floor(n/2) squares get subtracted
        return sum(sq[neg:]) - sum(sq[:neg])