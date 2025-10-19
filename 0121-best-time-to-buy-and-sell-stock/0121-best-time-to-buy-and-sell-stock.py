class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previous_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < previous_price:
                previous_price = prices[i]
                continue
            
            profit = prices[i] - previous_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit