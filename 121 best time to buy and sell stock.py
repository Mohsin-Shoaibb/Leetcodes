class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bestbuy = 0
        max_profit = 0

        for i in range(n):
            if prices[bestbuy] > prices[i]:
                bestbuy = i
            elif prices[i] - prices[bestbuy] > max_profit:
                max_profit = prices[i] - prices[bestbuy]
        
        return max_profit
