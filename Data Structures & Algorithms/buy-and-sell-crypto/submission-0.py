class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1 * float('inf')
        i = 0
        j = 1
        while j < len(prices):
            max_profit = max(max_profit, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
            j += 1
        return max(0, max_profit)