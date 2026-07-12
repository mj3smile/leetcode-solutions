class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [True for _ in range(n - 2)]
        i = 2
        while i * i <= n:
            if primes[i - 2]:
                for j in range(i * i, n, i):
                    primes[j - 2] = False
            i += 1
        
        result = 0
        for p in primes:
            if p:
                result += 1
        
        return result
            