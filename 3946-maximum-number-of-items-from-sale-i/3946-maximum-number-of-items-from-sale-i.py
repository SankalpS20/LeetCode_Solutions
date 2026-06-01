from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MAXF = 1500

        freq = [0] * (MAXF + 1)
        for f, _ in items:
            freq[f] += 1

        multiples_count = [0] * (MAXF + 1)
        for f in range(1, MAXF + 1):
            s = 0
            for m in range(f, MAXF + 1, f):
                s += freq[m]
            multiples_count[f] = s

        NEG = -10**18
        dp = [NEG] * (budget + 1)
        dp[0] = 0

        for factor, price in items:
            bonus = multiples_count[factor] - 1

            ndp = dp[:]

            p = price

            for rem in range(p):
                best = NEG
                q = 0
                pos = rem

                while pos <= budget:
                    if q > 0 and best != NEG:
                        ndp[pos] = max(ndp[pos], bonus + q + best)
                    if dp[pos] != NEG:
                        best = max(best, dp[pos] - q)

                    q += 1
                    pos += p

            dp = ndp

        return max(dp)