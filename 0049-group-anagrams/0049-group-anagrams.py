class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        group_index = dict()

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in group_index:
                result[group_index[sorted_word]].append(word)
            else:
                group_index[sorted_word] = len(result)
                result.append([word])

        return result