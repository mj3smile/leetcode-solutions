class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(parentheses, pair, open_parentheses, close_parentheses):
            pair += parentheses
            if len(pair) == n * 2:
                result.append(pair)
                return
            
            if parentheses == "(": 
                open_parentheses += 1
            else:
                close_parentheses += 1
                        
            if open_parentheses < n:
                dfs("(", pair, open_parentheses, close_parentheses)
            if close_parentheses < open_parentheses:
                dfs(")", pair, open_parentheses, close_parentheses)
        
        dfs("(", "", 0, 0)
        return result
        