class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            va = int(a[i]) if i >= 0 else 0
            vb = int(b[j]) if j >= 0 else 0
            s = va + vb + carry
            res.append(str(s % 2))
            carry = s // 2
            i -= 1
            j -= 1
            
        return ''.join(reversed(res))
