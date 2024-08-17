class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        open_parentheses = list()
        
        for c in s:
            if c not in pairs:
                open_parentheses.append(c)
                continue
            
            last_stack_item = ''
            if len(open_parentheses) > 0:
                last_stack_item = open_parentheses.pop()
                
            if last_stack_item != pairs[c]:
                return False
        
        return True if len(open_parentheses) == 0 else False