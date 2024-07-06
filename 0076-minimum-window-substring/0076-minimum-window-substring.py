class Solution:
    def __init__(self):
        self.t_cache = dict()
        self.s_cache = dict()
        self.s_cache_total = 0
        
    def minWindow(self, s: str, t: str) -> str:
        for i in t:
            self.t_cache[i] = self.t_cache.get(i, 0) + 1
        
        result = ''
        result_len = len(s)
        l = 0
        for r in range(len(s)):
            if s[r] in self.t_cache:
                self.increaseSKey(s[r])
            elif len(self.s_cache) == 0:
                l += 1
            
            while len(self.s_cache) == len(self.t_cache) and self.s_cache_total >= len(t):
                if r - l + 1 <= result_len:
                    result = s[l:r+1]
                    result_len = r - l + 1

                self.decreaseSKey(s[l])
                l += 1
                while l < r and s[l] not in self.s_cache:
                    l += 1
        
        return result
            
    def increaseSKey(self, s_key):
        self.s_cache[s_key] = self.s_cache.get(s_key, 0) + 1
        if self.s_cache[s_key] <= self.t_cache[s_key]:
            self.s_cache_total += 1
        
    def decreaseSKey(self, s_key):
        if self.s_cache[s_key] == self.t_cache[s_key]:
            self.s_cache_total -= 1
                
        self.s_cache[s_key] -= 1
        if self.s_cache[s_key] <= 0:
            del self.s_cache[s_key]
                