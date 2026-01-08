class Solution:
    def climbStairs(self, n: int) -> int:
        return self.waysToTop(n, dict())
    
    def waysToTop(self, n, cache):
        if n <= 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self.waysToTop(n - 1, cache) + self.waysToTop(n - 2, cache)
        return cache[n]