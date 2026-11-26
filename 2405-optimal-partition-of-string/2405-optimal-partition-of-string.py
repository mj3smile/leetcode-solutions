class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        chars = set()

        for c in s:
            if c in chars:
                result += 1
                chars = set()
            chars.add(c)
        
        return result