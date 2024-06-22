class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        
        l = 0
        for r in range(1, len(prices)):
            if prices[r] <= prices[l]:
                l = r
                continue
            
            result = max(result, prices[r] - prices[l])
        
        return result