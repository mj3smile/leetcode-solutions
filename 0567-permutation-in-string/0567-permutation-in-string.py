class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = dict()
        for s in s1:
            s1_letters[s] = s1_letters.get(s, 0) + 1
        
        l = 0
        window_cache = dict()
        for r in range(len(s2)):
            right = s2[r]
            window_cache[right] = window_cache.get(right, 0) + 1

            if r - l + 1 < len(s1):
                continue
            
            if window_cache == s1_letters:
                return True
            
            left = s2[l]
            window_cache[left] -= 1
            if window_cache[left] == 0:
                del window_cache[left]

            l += 1

        return False