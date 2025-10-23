class Solution:
    def countBits(self, n: int) -> List[int]:
        result = list()
        for i in range(n + 1):
            if self.isPowerOfTwo(i):
                result.append(1)
            else:
                result.append(self.countOneBit(i))
        return result

    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0
    
    def countOneBit(self, n):
        result = 0
        while n > 0:
            if n & 1 == 1:
                result += 1
            n = n // 2
        return result