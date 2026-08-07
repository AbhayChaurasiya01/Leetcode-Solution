from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter([2]),
    3: Counter([3]),
    4: Counter([2, 2]),
    5: Counter([5]),
    6: Counter([2, 3]),
    7: Counter([7]),
    8: Counter([2, 2, 2]),
    9: Counter([3, 3]),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeCount, ok = self._getPrimeCount(t)
        if not ok:
            return "-1"

        factorCount = self._getFactorCount(primeCount)

        if sum(factorCount.values()) > len(num):
            return "".join(d * c for d, c in factorCount.items())

        prefix = Counter()
        for ch in num:
            prefix += FACTOR_COUNTS[int(ch)]

        firstZero = next((i for i, ch in enumerate(num) if ch == "0"), len(num))

        if firstZero == len(num) and primeCount <= prefix:
            return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            prefix -= FACTOR_COUNTS[d]

            remain = len(num) - i - 1

            if i > firstZero:
                continue

            for nd in range(d + 1, 10):
                need = self._getFactorCount(
                    primeCount - prefix - FACTOR_COUNTS[nd]
                )

                if sum(need.values()) <= remain:
                    ones = remain - sum(need.values())

                    return (
                        num[:i]
                        + str(nd)
                        + "1" * ones
                        + "".join(x * c for x, c in need.items())
                    )

        factorCount = self._getFactorCount(primeCount)

        return (
            "1" * (len(num) + 1 - sum(factorCount.values()))
            + "".join(x * c for x, c in factorCount.items())
        )

    def _getPrimeCount(self, t: int):
        cnt = Counter()

        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                cnt[p] += 1

        return cnt, t == 1

    def _getFactorCount(self, cnt):
        c8, rem2 = divmod(cnt[2], 3)
        c9, c3 = divmod(cnt[3], 2)
        c4, c2 = divmod(rem2, 2)

        c6 = 0

        if c2 == 1 and c3 == 1:
            c2 = 0
            c3 = 0
            c6 = 1

        if c3 == 1 and c4 == 1:
            c2 = 1
            c6 = 1
            c3 = 0
            c4 = 0

        return {
            "2": c2,
            "3": c3,
            "4": c4,
            "5": cnt[5],
            "6": c6,
            "7": cnt[7],
            "8": c8,
            "9": c9,
        }