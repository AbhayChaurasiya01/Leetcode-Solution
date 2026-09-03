class Solution(object):

    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """

        mn = float('inf')

        # Find the smallest odd number
        for x in nums1:
            if x % 2 == 1:
                mn = min(mn, x)

        # If an even number is smaller than the
        # smallest odd number, it is impossible
        for x in nums1:
            if x % 2 == 0 and mn != float('inf') and x < mn:
                return False

        return True