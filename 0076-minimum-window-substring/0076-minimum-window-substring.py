class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cache = dict()
        for i in t:
            t_cache[i] = t_cache.get(i, 0) + 1
        
        s_cache = dict()
        s_cache_total = 0
        result = ''
        result_len = len(s)
        
        l = 0
        for r in range(len(s)):
            if s[r] in t_cache:
                s_cache[s[r]] = s_cache.get(s[r], 0) + 1
                if s_cache[s[r]] <= t_cache[s[r]]:
                    s_cache_total += 1
            elif len(s_cache) == 0:
                l += 1
            
            while len(s_cache) == len(t_cache) and s_cache_total >= len(t):
                if r - l + 1 <= result_len:
                    result = s[l:r+1]
                    result_len = r - l + 1

                if s_cache[s[l]] == t_cache[s[l]]:
                    s_cache_total -= 1
                s_cache = self.removeKey(s_cache, s[l])
                l += 1
                while l < r and s[l] not in s_cache:
                    l += 1
        
        return result
            
    
    def removeKey(self, s_cache, s_key):
        s_cache[s_key] -= 1
        if s_cache[s_key] <= 0:
            del s_cache[s_key]
        return s_cache
                