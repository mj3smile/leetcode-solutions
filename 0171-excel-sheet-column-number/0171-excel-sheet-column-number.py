class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        zero = ord('A') - 1
        result = 0

        for c in range(len(columnTitle)):
            if c > 0:
                result *= (ord('Z') - zero)
            
            result += (ord(columnTitle[c]) - zero)
        
        return result
