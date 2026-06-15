class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        [10, 5, 1, 7]
        buy_index = 0
        index = 0
        profit = 0

        while index < len(prices):
            if prices[buy_index] > prices[index]:
                buy_index = index
            elif prices[buy_index] < prices[index]:
                diff = prices[index] - prices [buy_index]
                profit =  diff if diff > profit else profit
            index = index + 1
        return profit
        