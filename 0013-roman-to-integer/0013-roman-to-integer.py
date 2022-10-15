class Solution:
    def romanToInt(self, s: str) -> int:
        index = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = index[s[len(s) -  1]]
        
        for i in range(len(s) - 1, 0, -1):
            pval = index[s[i - 1]]
            cval = index[s[i]]
            result += pval if pval >= cval else -pval
        
        return result