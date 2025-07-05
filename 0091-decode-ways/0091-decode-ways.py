class Solution:
    def numDecodings(self, s: str) -> int:
        self.message = s
        self.cache = dict()
        return self.decodeWays(0)
    
    def decodeWays(self, index) -> int:
        if index in self.cache:
            return self.cache[index]

        if index == len(self.message):
            return 1
        
        curr_message = self.message[index]
        if curr_message == '0':
            return 0

        result = self.decodeWays(index + 1)
        if index < len(self.message) - 1 and (curr_message == '1' or (curr_message == '2' and self.message[index + 1] in {'0', '1', '2', '3', '4', '5', '6'})):
            result += self.decodeWays(index + 2)
        
        self.cache[index] = result
        return result
