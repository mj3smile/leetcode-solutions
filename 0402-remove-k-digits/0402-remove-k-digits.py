class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            if n != "0" or stack:
                stack.append(n)
            
        while k > 0 and stack:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        return "".join(stack)