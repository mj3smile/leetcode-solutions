class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        sumWeights = sum(weights)
        maxCap = sumWeights
        minCap = 0
        for w in weights:
            sumWeights += w
            minCap = max(minCap, w)

        # minCap = sumWeights // days
        # if sumWeights % days > 0:
        #     minCap += 1
        
        left, right = minCap, maxCap
        while left < right:
            # print("==============")
            # print("left:", left, "right:", right)
            mid = (left + right) // 2
            daysToShip = self.daysToShip(mid)
            # print("cap:", mid, "daysToShip:", daysToShip)

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