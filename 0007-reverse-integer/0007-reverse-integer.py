class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            x = x * -1
            sign = -1
        
        min_limit = 2**31 * -1
        max_limit = 2**31 - 1

        reversed = 0
        while x > 0:
            reversed = reversed * 10 + (x % 10)
            x = x // 10
        
        reversed = reversed * sign
        # print(f"result: {reversed}, min limit: {min_limit}, max limit: {max_limit}")
        if reversed < min_limit or reversed > max_limit:
            return 0
        
        return reversed
        