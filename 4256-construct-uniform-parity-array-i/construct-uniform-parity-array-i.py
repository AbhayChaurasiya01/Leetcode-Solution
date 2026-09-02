class Solution(object):

    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """

        has_odd = False
        has_even = False

        for num in nums1:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True

        # If all numbers have the same parity,
        # nums1 itself can be used as nums2.
        if not has_odd or not has_even:
            return True

        # If both odd and even numbers exist,
        # subtract an opposite-parity number from each element.
        # odd - even = odd
        # even - odd = odd
        # Therefore, all elements can be made odd.
        return True