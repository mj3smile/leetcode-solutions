class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for price in prices:
            if price < buy_price:
                buy_price = price
            
            profit = max(profit, price - buy_price)
        
        return profit