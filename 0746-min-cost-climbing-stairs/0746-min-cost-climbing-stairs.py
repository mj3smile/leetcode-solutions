class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down
        cache = dict()
        def climb(staircase):
            if staircase >= len(cost):
                return 0
            if staircase in cache:
                return cache[staircase]
            
            total = cost[staircase]
            total += min(climb(staircase + 1), climb(staircase + 2))
            cache[staircase] = total
            
            return total
        
        return min(climb(0), climb(1))
        
#         cost.append(0)
#         costs = [cost[0], cost[1]]
        
#         for c in range(2, len(cost)):
#             tmp = cost[0]
#             costs[0] += costs[1]
#             costs[1] +=
        
#         return min(costs)
            