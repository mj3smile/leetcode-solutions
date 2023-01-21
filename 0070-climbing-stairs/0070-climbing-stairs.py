class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        
        # we only count when staircase >= 4
        # steps[0] == steps to climb stair with 2 staircase
        # steps[1] == steps to climb stair with 3 staircase
        steps = [2, 3]
        for _ in range(n + 1 - 4):
            tmp = steps[1]
            steps[1] = steps[0] + steps[1]
            steps[0] = tmp
        return steps[1]