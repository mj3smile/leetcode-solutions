class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = dict()

        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = t[i]
            elif map[s[i]] != t[i]:
                return False
        
        return True