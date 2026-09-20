class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            position = i+1
            ans += value * position
        return ans
        