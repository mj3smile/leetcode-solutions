class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        left = 0
        for right in range(1, len(prices)):
            if prices[left] >= prices[right]:
                left = right
                continue
            
            result += prices[right] - prices[left]
            left = right
        
        return result