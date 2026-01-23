class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        anagramIndex = dict()
        for s in strs:
            key = self.getKey(s)
            if key not in anagramIndex:
                anagramIndex[key] = len(result)
                result.append([s])
            else:
                result[anagramIndex[key]].append(s)
        return result

    def getKey(self, s):
        pos = [0 for i in range(ord('z') - ord('a') + 1)]
        for i in s:
            pos[ord(i) - ord('a')] += 1
        return tuple(pos)