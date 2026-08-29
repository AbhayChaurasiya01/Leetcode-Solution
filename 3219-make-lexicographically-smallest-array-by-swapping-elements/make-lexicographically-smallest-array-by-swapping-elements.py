class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        pairs = [(nums[i], i) for i in range(n)]
        pairs.sort()

        ans = [0] * n

        i = 0

        while i < n:
            j = i

            # Find one connected group
            while j + 1 < n and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1

            # Original indices of this group
            indices = [pairs[k][1] for k in range(i, j + 1)]
            indices.sort()

            # Smallest values -> smallest original indices
            for k in range(j - i + 1):
                ans[indices[k]] = pairs[i + k][0]

            i = j + 1

        return ans

