class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openParentheses = list()
        result = list()

        for char in s:
            if char != "(" and char != ")":
                result.append(char)
                continue
            
            if char == "(":
                openParentheses.append(len(result))
                result.append("")
            elif openParentheses:
                result[openParentheses.pop()] = "("
                result.append(")")
        
        return "".join(result)