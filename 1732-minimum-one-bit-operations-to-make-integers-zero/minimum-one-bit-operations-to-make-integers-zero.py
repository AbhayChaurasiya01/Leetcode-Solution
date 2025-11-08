class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        highest = 0
        while (1 << (highest + 1)) <= n:
            highest += 1
        mask = 1 << highest
        return (1 << (highest + 1)) - 1 - self.minimumOneBitOperations(n ^ mask)
