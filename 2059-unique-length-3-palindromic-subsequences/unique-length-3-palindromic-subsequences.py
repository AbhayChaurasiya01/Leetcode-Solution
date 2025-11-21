class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        last = {}

        # Record first and last occurrence of each character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0

        # For each character, count unique chars between first and last position
        for ch in first:
            if last[ch] > first[ch]:
                mid_chars = set(s[first[ch] + 1 : last[ch]])
                ans += len(mid_chars)

        return ans
