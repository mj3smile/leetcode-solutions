class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def isSubsequenceOf(t, s):
            tp, sp = 0, 0
            new_t = ""

            while tp < len(t) and sp < len(s):
                if t[tp] == s[sp]:
                    new_t += s[sp]
                    tp += 1
                    sp += 1
                else:
                    sp += 1
                    
            return t == new_t
        
        result = 0
        i, j = 0, 0
        while i < len(target):
            subsequence = False
            while j < len(target) and isSubsequenceOf(target[i:j+1], source):
                subsequence = True
                j += 1
            if not subsequence:
                return -1
            result += 1
            i = j
        
        return result