class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        
        for i in range(1, n + 1):
            x = i
            while x > 0:
                if x & 1 == 1:
                    result[i] += 1
                x = x >> 1
        
        return result