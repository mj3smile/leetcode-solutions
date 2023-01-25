class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
    
        # top down
#         cache = dict()
#         def climb(staircase):
#             if staircase >= len(cost):
#                 return 0
#             if staircase in cache:
#                 return cache[staircase]
            
#             total = cost[staircase]
#             total += min(climb(staircase + 1), climb(staircase + 2))
#             cache[staircase] = total
            
#             return total
        
#         return min(climb(0), climb(1))
            