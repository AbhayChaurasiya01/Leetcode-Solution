
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]

            result = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = solve(expr[:i])
                    right = solve(expr[i+1:])

                    for a in left:
                        for b in right:
                            if ch == '+':
                                result.append(a + b)
                            elif ch == '-':
                                result.append(a - b)
                            else:
                                result.append(a * b)

            if not result:
                result.append(int(expr))

            memo[expr] = result
            return result

        return solve(expression)
