class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            key = self.getGroupKey(word)
            groups[key] = groups.get(key, list())
            groups[key].append(word)
        
        result = list()
        for key in groups:
            result.append(groups[key])
        
        return result


    
    def getGroupKey(self, word):
        char_to_frequency = [0] * (ord("z") - ord("a") + 1)
        for s in word:
            index = ord(s) - ord("a")
            char_to_frequency[index] += 1
        return tuple(char_to_frequency)