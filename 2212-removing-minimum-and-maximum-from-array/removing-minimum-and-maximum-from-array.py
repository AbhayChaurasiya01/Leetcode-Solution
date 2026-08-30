class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Delete both from the left
        option1 = right + 1

        # Delete both from the right
        option2 = n - left

        # Delete one from each side
        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)