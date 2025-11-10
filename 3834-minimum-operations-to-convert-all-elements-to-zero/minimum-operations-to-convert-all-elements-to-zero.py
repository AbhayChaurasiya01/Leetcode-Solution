class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        stack = [0]              # sentinel zero to simplify logic
        for num in nums:
            # remove all bigger layers that can't continue past this smaller num
            while stack and stack[-1] > num:
                stack.pop()
            # if current value starts a new layer, count an operation
            if stack[-1] < num:
                ans += 1
                stack.append(num)
        return ans
