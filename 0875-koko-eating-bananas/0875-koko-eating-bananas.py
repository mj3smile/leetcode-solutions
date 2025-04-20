class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = left
        
        while left <= right:
            mid = (left + right) // 2
            duration = self.getEatingDuration(piles, mid)

            if duration <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        
    def getEatingDuration(self, piles, rate):
        result = 0

        for p in piles:
            if p == 0:
                continue

            if p < rate:
                result += 1
                continue

            result += p // rate
            if p % rate > 0:
                result += 1
        
        return result
            