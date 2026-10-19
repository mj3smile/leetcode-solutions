class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        result = []
        n = len(costs)

        cache = dict()
        def pick(index, color):
            if index == n:
                return 0
            if (index, color) in cache:
                return cache[(index, color)]
            
            candidate1, candidate2 = 0, 1
            if color == 0:
                candidate1, candidate2 = 1, 2
            elif color == 1:
                candidate1, candidate2 = 0, 2

            cost1 = pick(index + 1, candidate1)
            cost2 = pick(index + 1, candidate2)
            total = costs[index][color] + min(cost1, cost2)
            cache[(index, color)] = total
            return total
            
        return min(pick(0, 0), pick(0, 1), pick(0, 2))