class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        [10, 5, 1, 7]
        low_stock_index = 0
        index = 0
        profit = 0

        while index < len(prices):
            if prices[low_stock_index] > prices[index]:
                low_stock_index = index
            elif prices[low_stock_index] < prices[index]:
                diff = prices[index] - prices [low_stock_index]
                profit =  diff if diff > profit else profit
            index = index + 1
        return profit
        