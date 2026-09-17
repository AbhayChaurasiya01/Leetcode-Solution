
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        best = [float('inf')] * n

        prefix = 0
        left = 0
        answer = float('inf')

        for right in range(n):
            prefix += arr[right]

            while prefix > target:
                prefix -= arr[left]
                left += 1

            if prefix == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])

                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if answer == float('inf') else answer