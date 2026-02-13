class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitLetters = dict()
        counter = 0
        for i in range(2, 10):
            length = 3
            if i == 7 or i == 9:
                length = 4
            for _ in range(length):
                digitLetters[str(i)] = digitLetters.get(str(i), [])
                digitLetters[str(i)].append(string.ascii_lowercase[counter])
                counter += 1
        
        result = list()
        def combination(index, com):
            if index == len(digits):
                result.append(com)
                return
            for l in digitLetters[digits[index]]:
                combination(index + 1, com + l)
        combination(0, "")
        return result