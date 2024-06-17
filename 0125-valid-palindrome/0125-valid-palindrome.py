class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while True:
            if left > right:
                break
            
            lchar = s[left].lower()
            lcode = ord(lchar)
            if (lcode < 97 or lcode > 122) and (lcode < 48 or lcode > 57):
                left += 1
                continue
            
            rchar = s[right].lower()
            rcode = ord(rchar)
            if (rcode < 97 or rcode > 122) and (rcode < 48 or rcode > 57):
                right -= 1
                continue
            
            if lchar != rchar:
                return False
            
            left += 1
            right -= 1
        
        return True