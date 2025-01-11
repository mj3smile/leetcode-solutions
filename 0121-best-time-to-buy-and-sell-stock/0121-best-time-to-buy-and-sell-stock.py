class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        max_price = 0
        max_price_index = -1
        for l in range(len(prices)):
            if max_price_index > l:
                result = max(result, max_price - prices[l])
                continue
            
            for r in range(l + 1, len(prices)):
                if prices[r] > max_price:
                    max_price = prices[r]
                    max_price_index = r
                result = max(result, prices[r] - prices[l])
        
        return result