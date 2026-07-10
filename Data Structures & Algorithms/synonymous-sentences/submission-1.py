class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        pairs = dict()

        for p1, p2 in synonyms:
            if p1 in pairs and p2 in pairs:
                pairs[p1].update(pairs[p2])
                pairs[p2].update(pairs[p1])
            elif p1 in pairs:
                pairs[p1].add(p2)
                pairs[p2] = pairs[p1]
            elif p2 in pairs:
                pairs[p2].add(p1)
                pairs[p1] = pairs[p2]
            else:
                pairs[p1] = {p1, p2}
                pairs[p2] = pairs[p1]
        
        # print(pairs)
        result = list()
        words = text.split()
        def construct(index, sentence):
            if index == len(words):
                result.append(" ".join(sentence))
                return
            
            if words[index] not in pairs:
                sentence.append(words[index])
                construct(index + 1, sentence)
                sentence.pop()
            else:
                for p in pairs[words[index]]:
                    # if p == words[index]:
                    #     continue
                    sentence.append(p)
                    construct(index + 1, sentence)
                    sentence.pop()
        
        construct(0, [])
        result.sort()
        return result