class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        maxNum = max(nums)
        isPrimes = [True for _ in range(maxNum + 1)]
        isPrimes[0] = isPrimes[1] = False

        for i in range(2, int(maxNum**0.5) + 1):
            if isPrimes[i]:
                for j in range(i * i, maxNum + 1, i):
                    isPrimes[j] = False
        
        primes = list()
        for i in range(len(isPrimes)):
            if isPrimes[i]:
                primes.append(i)
        
        def pickPrimes(startRange, endRange):
            l, r = 0, len(primes) - 1
            while l < r:
                mid = (l + r) // 2

                if primes[mid] == startRange:
                    l = mid
                    break
                elif primes[mid] > startRange:
                    r = mid
                else:
                    l = mid + 1
            
            if primes[l] >= endRange:
                return primes[l - 1]

            return primes[l]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            
            if nums[i] <= 2:
                continue

            diff = nums[i] - nums[i + 1]
            prime = pickPrimes(diff + 1, nums[i])
            nums[i] -= prime
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True