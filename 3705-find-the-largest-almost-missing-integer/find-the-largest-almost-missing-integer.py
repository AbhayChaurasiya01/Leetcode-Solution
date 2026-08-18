class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)

        count = Counter(nums)

        if k == 1:
            ans = -1
            for x in nums:
                if count[x] == 1:
                    ans = max(ans, x)
            return ans

        ans = -1

        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans