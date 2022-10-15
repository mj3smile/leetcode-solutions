class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        started = False
        minus = False
        
        for c in s:
            if c == "+" and not started:
                started = True
                continue
                
            if c == "-" and not started:
                started = minus = True
                continue
                
            if not c in nums and c == " ":
                if not started:
                    continue
                else:
                    break
            
            if not c in nums and c != " ":
                break
            
            i = i * 10 + (ord(c) - ord("0"))
            started = True
            
        if minus: i = -i
        if i < -2**31: return -2**31
        if i > 2**31 - 1: return 2**31 - 1
        
        return i
            