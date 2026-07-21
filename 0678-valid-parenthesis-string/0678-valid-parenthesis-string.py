class Solution:
    def checkValidString(self, s: str) -> bool:
        open_parenthesis = list()
        asterisk = 0

        for c in s:
            if c == "(":
                open_parenthesis.append(c)
                continue
            if c == "*":
                asterisk += 1
                continue
            
            if not open_parenthesis and asterisk == 0:
                return False
            
            if open_parenthesis:
                open_parenthesis.pop()
            else:
                asterisk -= 1
        
        close_parenthesis = list()
        asterisk = 0

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == ")":
                close_parenthesis.append(c)
                continue
            if c == "*":
                asterisk += 1
                continue
            
            if not close_parenthesis and asterisk == 0:
                return False
            
            if close_parenthesis:
                close_parenthesis.pop()
            else:
                asterisk -= 1
        
        return True
        # if not open_parenthesis:
        #     return True
        
        # print("here", len(open_parenthesis), asterisk)
        # (((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))))((*(((((
        # return len(open_parenthesis) <= asterisk