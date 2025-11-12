class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # If there's at least one 1, each non-1 can be turned into 1 in one operation
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # If overall GCD > 1, impossible to make any element 1
        g_all = 0
        for x in nums:
            g_all = gcd(g_all, x)
        if g_all != 1:
            return -1
        
        # Find shortest subarray with gcd == 1
        # For subarray nums[i..j], number of operations to create a 1 from it is (j - i)
        min_ops_to_create_one = float('inf')
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_ops_to_create_one = min(min_ops_to_create_one, j - i)
                    break  # no need to extend this i further
        
        # After creating one (cost = min_ops_to_create_one), we need (n - 1) additional ops
        # to spread that 1 to all other elements.
        return min_ops_to_create_one + (n - 1)