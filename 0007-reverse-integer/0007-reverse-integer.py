class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1
        
        if x < 0:
            sign = -1
            x *= -1
        
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result * sign