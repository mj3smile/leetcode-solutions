class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        prev = prices[0]

        for i in range(1, len(prices)):
            if prev < prices[i]:
                result += (prices[i] - prev)
            prev = prices[i]
        
        return result