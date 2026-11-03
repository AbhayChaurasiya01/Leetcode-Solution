
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for ch in s:
            if ch == '[':
                count += 1
            elif count > 0:
                count -= 1

        return (count + 1) // 2
