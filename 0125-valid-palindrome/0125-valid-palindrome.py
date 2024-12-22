class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ""
        for c in s:
            unicode_decimal = ord(c)
            if ((unicode_decimal < 48 or unicode_decimal > 57) 
            and (unicode_decimal < 65 or unicode_decimal > 90)
            and (unicode_decimal < 97 or unicode_decimal > 122)):
                continue

            sentence += c.lower()
        
        for i in range(len(sentence) // 2):
            left, right = sentence[i], sentence[len(sentence) - i - 1]
            if left != right:
                return False
        
        return True