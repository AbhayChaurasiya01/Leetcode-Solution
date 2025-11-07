class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Step 1: Compute initial power for each city using sliding window
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]
        
        power = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            power[i] = prefix[right] - prefix[left]
        
        # Step 2: Check function - can we make all cities at least 'x' powered?
        def can(x):
            added = [0] * (n + 1)
            curr_add = 0
            remain = k
            
            for i in range(n):
                curr_add += added[i]
                curr_power = power[i] + curr_add
                if curr_power < x:
                    need = x - curr_power
                    if need > remain:
                        return False
                    remain -= need
                    curr_add += need
                    if i + 2 * r + 1 <= n - 1:
                        added[i + 2 * r + 1] -= need
            return True
        
        # Step 3: Binary search on answer
        low, high = 0, sum(stations) + k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
