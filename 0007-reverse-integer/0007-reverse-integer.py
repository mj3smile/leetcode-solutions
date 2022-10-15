class Solution:
    def reverse(self, x: int) -> int:
        signed = x < 0
        reversed_x = 0
        
        if signed: x *= -1
        while x > 0:
            reversed_x = (reversed_x * 10) + (x % 10)
            x = x // 10
        
        if reversed_x > 2**31 - 1: return 0
        return reversed_x if not signed else -reversed_x