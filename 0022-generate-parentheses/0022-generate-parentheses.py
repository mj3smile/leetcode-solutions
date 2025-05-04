class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.cache = set()
        self.result = list()
        self.generatePairs("(", "", [], 0)

        return self.result
    
    def generatePairs(self, char, pairs, stack, count):
        if len(pairs) == self.n * 2:
            if pairs not in self.cache: 
                self.result.append(pairs)
                self.cache.add(pairs)
            return
        
        if (char == "(" and count == self.n) or (char == ")" and len(stack) == 0):
            return

        stack = stack.copy()
        if char == "(":
            stack.append(char)
            count += 1
        else:
            stack.pop()
        
        pairs += char
        self.generatePairs("(", pairs, stack, count)
        self.generatePairs(")", pairs, stack, count)
            