class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        longest_sub = 0
        
        for i in range(len(s)):
            def find_palindrome(left, right, longest_sub, result):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > longest_sub:
                        result = s[left:right + 1]
                        longest_sub = right - left + 1

                    left -= 1
                    right += 1
                
                return result, longest_sub
                
            ## odd substring length
            result, longest_sub = find_palindrome(i, i, longest_sub, result)
            
            ## even
            result, longest_sub = find_palindrome(i, i + 1, longest_sub, result)
            
        
        return result