class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            time = self.getEatTime(mid)
            if time == self.h or time < self.h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
    
    def getEatTime(self, rate: int) -> int:
        total = 0
        for p in self.piles:
            total += p // rate
            if p % rate > 0:
                total += 1
        return total
