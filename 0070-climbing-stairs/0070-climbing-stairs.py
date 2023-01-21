class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        steps = [2, 3]
        i = 4
        while i <= n:
            tmp = steps[1]
            steps[1] = steps[0] + steps[1]
            steps[0] = tmp
            i += 1
        return steps[1]