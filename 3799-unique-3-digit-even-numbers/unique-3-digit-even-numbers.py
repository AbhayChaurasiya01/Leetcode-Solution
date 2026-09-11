class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue

                for k in range(len(digits)):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        ans.add(num)

        return len(ans)