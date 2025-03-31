class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        n = len(prices)
        buy = 0
        for sell in range(1, n):
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit) 
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1

        return maxprofit