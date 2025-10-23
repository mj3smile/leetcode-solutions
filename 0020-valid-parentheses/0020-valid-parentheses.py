class Solution:
    def isValid(self, s: str) -> bool:
        close_parentheses = {")": "(", "}": "{", "]": "["}
        open_parentheses = []

        for char in s:
            if char not in close_parentheses:
                open_parentheses.append(char)
            elif len(open_parentheses) == 0 or open_parentheses.pop() != close_parentheses[char]:
                return False
        
        return len(open_parentheses) == 0