class Solution:
    def minOperations(self, s: str) -> int:
        t = ''.join(sorted(s))
        
        if s == t:
            return 0
        
        n = len(s)
        if n == 2:
            return -1
        
        # If first or last character is already in its correct sorted position
        if t[0] == s[0] or t[-1] == s[-1]:
            return 1
        
        # Try sorting first n-1 chars, then last n-1 chars
        s1 = s[:n-1]
        s1 = ''.join(sorted(s1)) + s[-1]
        s1 = s1[0] + ''.join(sorted(s1[1:]))
        
        # Try the reverse order
        s2 = s[0] + ''.join(sorted(s[1:]))
        s2 = ''.join(sorted(s2[:n-1])) + s2[-1]
        
        if s1 == t or s2 == t:
            return 2
        
        return 3