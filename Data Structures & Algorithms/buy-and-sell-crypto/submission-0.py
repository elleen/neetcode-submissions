class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for i, price in enumerate(prices):
            if price < lowest_price:
                lowest_price = price
            elif price - lowest_price > max_profit:
                max_profit = price - lowest_price

        return max_profit