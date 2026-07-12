class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for _ in range(2, right + 1)]
        i = 2
        while i * i <= right:
            if prime[i - 2]:
                for j in range(i * i, right + 1, i):
                    prime[j - 2] = False
            i += 1
        
        # p = []
        # for i in range(len(prime)):
        #     if prime[i]:
        #         p.append(i + 2)
        
        # print("primes", p)
        
        nums = []
        result = []
        for i in range(left, right + 1):
            if i < 2 or not prime[i - 2]:
                continue
            
            # print("prime", i)
            nums.append(i)
            if len(nums) <= 2:
                result.append(i)
            
            if len(result) < 2:
                continue
            
            if (nums[-1] - nums[-2]) < (result[-1] - result[-2]):
                result = [nums[-2], nums[-1]]
        
        if len(result) < 2:
            return [-1, -1]
        
        return result
            