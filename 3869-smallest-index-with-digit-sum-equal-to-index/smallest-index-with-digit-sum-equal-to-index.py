class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = 0
            n = num
            while n > 0:
                digit_sum += n % 10
                n //= 10
            if digit_sum == i:
                return i
        return -1