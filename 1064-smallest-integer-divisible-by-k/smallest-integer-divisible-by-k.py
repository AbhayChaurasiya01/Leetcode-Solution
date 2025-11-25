class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        # Numbers made of only '1' can never be divisible by 2 or 5
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        rem = 1 % K
        length = 1
        
        # At most K different remainders are possible
        while length <= K:
            if rem == 0:
                return length
            rem = (rem * 10 + 1) % K
            length += 1
        
        return -1
