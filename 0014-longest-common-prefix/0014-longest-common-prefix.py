class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            if prefix == word:
                continue
            
            i = 0
            new_prefix = ""
            for i in range(len(min(prefix, word))):
                if prefix[i] != word[i]:
                    break
                new_prefix += prefix[i]
            
            prefix = new_prefix
        
        return prefix