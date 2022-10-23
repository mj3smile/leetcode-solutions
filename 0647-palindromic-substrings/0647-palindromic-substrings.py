class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        def find_palindrome(left, right, result):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            return result

                        
        for i in range(len(s)):    
            ## odd substring length
            result = find_palindrome(i, i, result)
            
            ## even
            result = find_palindrome(i, i + 1, result)
        
        return result