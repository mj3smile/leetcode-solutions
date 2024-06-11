class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        
        for word in strs:
            indices = [0] * 26
            for char in word:
                indices[ord(char) - ord('a')] += 1
            
            key = tuple(indices)
            result[key] = result.get(key, [])
            result[key].append(word)
        
        return result.values()
            