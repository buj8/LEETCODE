class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxprofit = 0
        while sell < len(prices):
            if prices[buy] >= prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                maxprofit = max(profit, maxprofit)
            sell += 1
        return maxprofit