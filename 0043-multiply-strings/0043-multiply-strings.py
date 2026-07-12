class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0

        p1, p2 = 0, 0
        while p1 < len(num1) or p2 < len(num2):
            if p1 < len(num1):
                n = ord(num1[p1]) - ord("0")
                n1 = n1 * 10 + n
            if p2 < len(num2):
                n = ord(num2[p2]) - ord("0")
                n2 = n2 * 10 + n
            p1 += 1
            p2 += 1
        
        n3 =  n1 * n2
        if n3 == 0:
            return "0"
            
        result = ""
        base = ord("0")
        while n3 > 0:
            result = chr(base + (n3 % 10)) + result
            n3 = n3 // 10
        
        return result