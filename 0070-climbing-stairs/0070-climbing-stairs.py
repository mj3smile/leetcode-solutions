class Solution:
    def climbStairs(self, n: int) -> int:
        return self.waysToClimb(n, dict())

    def waysToClimb(self, n, cache):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = self.waysToClimb(n - 2, cache) + self.waysToClimb(n - 1, cache)
        return cache[n]