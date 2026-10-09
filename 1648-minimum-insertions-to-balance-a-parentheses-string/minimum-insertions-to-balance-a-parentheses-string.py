class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open_count = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:  # s[i] == ')'
                if i + 1 < n and s[i + 1] == ')':
                    # Found "))"
                    if open_count > 0:
                        open_count -= 1
                    else:
                        ans += 1  # insert '('
                    i += 2
                else:
                    # Single ')', need one more ')' to make "))"
                    ans += 1  # insert ')'
                    if open_count > 0:
                        open_count -= 1
                    else:
                        ans += 1  # insert '('
                    i += 1

        ans += open_count * 2  # each unmatched '(' needs "))"
        return ans