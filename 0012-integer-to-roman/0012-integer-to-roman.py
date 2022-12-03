class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        symbolToInt = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        
        limit_index = 0
        for i in range(len(symbols)):
            if symbolToInt[symbols[i]] > num: break
            limit_index = i
        
        # print(symbols[:limit_index + 1])
        result = ''
        while num > 0:
            sym = symbols[limit_index]
            subs = symbolToInt[sym]
            
            if num - subs >= 0:
                result += sym
                num -= subs
            else:
                limit_index -= 1
        
        return result
                
        