class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # minimum possible open parentheses count
        high = 0  # maximum possible open parentheses count

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # ch == '*'
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0