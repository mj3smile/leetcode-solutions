class Solution:
    def isValid(self, s: str) -> bool:
        closeParentheses = {"}": "{", "]": "[", ")": "("}
        stack = list()

        for char in s:
            if char not in closeParentheses:
                stack.append(char)
                continue
            if not stack or stack.pop() != closeParentheses[char]:
                return False
        
        return len(stack) == 0