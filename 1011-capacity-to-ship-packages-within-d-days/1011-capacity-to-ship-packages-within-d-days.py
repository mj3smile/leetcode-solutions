class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        maxCap = 0
        minCap = 0
        for w in weights:
            maxCap += w
            minCap = max(minCap, w)

        
        left, right = minCap, maxCap
        while left < right:
            mid = (left + right) // 2
            daysToShip = self.daysToShip(mid)

            if daysToShip > days:
                left = mid + 1
            else:
                right = mid

        return right

    def daysToShip(self, cap):
        days = 0
        currWeight = 0
        for w in self.weights:
            if currWeight + w > cap:
                days += 1
                currWeight = 0
            
            currWeight += w

        return days + 1