class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_stock_index = 0
        index = 0
        profit = 0

        while index < len(prices):
            if prices[low_stock_index] >= prices[index]:
                low_stock_index = index
                index = index + 1
                continue
            diff = prices[index] - prices [low_stock_index]
            profit = max(profit, diff)
            index = index + 1
        return profit
        