class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        # Required variable
        calendrix = s

        # Count characters
        left = [0] * 26

        for ch in s:
            left[ord(ch) - ord('a')] += 1

        # Find the middle character
        mid = ""

        for i in range(26):
            if left[i] % 2 == 1:
                if mid != "":
                    return ""

                mid = chr(ord('a') + i)
                left[i] -= 1

        # Try to make the left half equal to target's left half
        half = n // 2

        for i in range(half):
            c = ord(target[i]) - ord('a')
            left[c] -= 2

        # Count invalid characters and largest available character
        neg = 0
        left_max = -1

        for i in range(26):
            if left[i] < 0:
                neg += 1
            elif left[i] > 0:
                left_max = max(left_max, i)

        # Case 1:
        # Target's left half can be used exactly.
        # We only need to compare the right half.
        if neg == 0:

            left_part = target[:half]

            right_part = mid + left_part[::-1]

            if right_part > target[half:]:
                return left_part + right_part

        # Case 2:
        # Find the rightmost position that can be increased.
        for i in range(half - 1, -1, -1):

            c = ord(target[i]) - ord('a')

            # Restore the pair used at target[i]
            left[c] += 2

            # Update largest available character
            if left[c] == 2:
                left_max = max(left_max, c)

            # If some required character is unavailable,
            # we cannot keep the prefix equal.
            if neg > 0:
                # Check again whether all counts are valid
                neg = 0

                for x in range(26):
                    if left[x] < 0:
                        neg += 1

                if neg > 0:
                    continue

            # Need a character strictly greater than target[i]
            if left_max <= c:
                continue

            # Find smallest available character > target[i]
            j = c + 1

            while j < 26 and left[j] == 0:
                j += 1

            if j == 26:
                continue

            # Use j instead of target[i]
            left[j] -= 2

            # Build left half
            ans_left = list(target[:i + 1])
            ans_left[i] = chr(ord('a') + j)

            # Fill remaining pairs in ascending order
            for k in range(26):
                if left[k] > 0:
                    ch = chr(ord('a') + k)
                    ans_left.extend([ch] * (left[k] // 2))

            ans_left = ''.join(ans_left)

            # Mirror
            right = ans_left[::-1]

            return ans_left + mid + right

        return ""