class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0
        for r in range(1, len(prices)):
            maxp = max(maxp, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxp
