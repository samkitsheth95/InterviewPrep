from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit+prices[i]-prices[i-1], 0)
            maxProfit = max(maxProfit, profit)
        return maxProfit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
