class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(31, -1, -1):
            if n == 0:
                break
                
            if n & 1 == 1:
                result += 2**i
            n = n >> 1
        
        return result
        