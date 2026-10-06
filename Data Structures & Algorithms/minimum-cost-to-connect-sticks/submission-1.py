class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        cost = 0
        while len(sticks) > 1:
            stickA = heapq.heappop(sticks)
            stickB = heapq.heappop(sticks)
            cost += stickA + stickB
            heapq.heappush(sticks, stickA + stickB)
        
        return cost