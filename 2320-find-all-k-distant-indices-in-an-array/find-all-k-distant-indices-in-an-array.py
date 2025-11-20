class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_indices = []

        # collect all positions where nums[i] == key
        for i in range(n):
            if nums[i] == key:
                key_indices.append(i)

        ans = []
        j = 0
        m = len(key_indices)

        # two-pointer sweep to find all i such that |i - key_index| <= k
        for i in range(n):
            while j < m and key_indices[j] < i - k:
                j += 1
            if j < m and abs(key_indices[j] - i) <= k:
                ans.append(i)

        return ans
