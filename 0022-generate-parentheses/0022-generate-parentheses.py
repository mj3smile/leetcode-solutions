class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(par, pair, open_parentheses, close_parentheses):
            pair += par
            if len(pair) == n * 2:
                result.append(pair)
                return
            
            if par == "(": 
                open_parentheses += 1
            else:
                close_parentheses += 1
                        
            print(pair, open_parentheses, close_parentheses)
            if open_parentheses < n:
                dfs("(", pair, open_parentheses, close_parentheses)
            if close_parentheses < open_parentheses:
                dfs(")", pair, open_parentheses, close_parentheses)
        
        dfs("(", "", 0, 0)
        return result
        