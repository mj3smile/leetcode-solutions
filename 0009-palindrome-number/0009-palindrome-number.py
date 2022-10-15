class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reversed_n = 0
        
        while num > 0:
            reversed_n = (reversed_n * 10) + (num % 10)
            num = num // 10
        
        return x == reversed_n