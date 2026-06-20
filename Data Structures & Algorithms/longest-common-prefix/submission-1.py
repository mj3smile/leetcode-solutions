class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for w in range(1, len(strs)):
            if result == "":
                break

            word = strs[w]
            if len(result) > len(word) or word[:len(result)] != result:
                i, j = 0, 0
                while i < len(word) and word[i] == result[j]:
                    i, j = i+1, j+1
                result = result[:j]
        
        return result