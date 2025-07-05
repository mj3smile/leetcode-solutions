class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.dp = {len(s) : 1}
        return self.dfs(0)
    
    def dfs(self, i):
        if i in self.dp:
            return self.dp[i]
        if self.s[i] == "0":
            return 0

        res = self.dfs(i + 1)
        if i + 1 < len(self.s) and (
            self.s[i] == "1" or self.s[i] == "2" and
            self.s[i + 1] in "0123456"
        ):
            res += self.dfs(i + 2)
        self.dp[i] = res
        return res
    #     self.message = s
    #     return self.decodeWays(0)
        
    
    # def decodeWays(self, index) -> int:
    #     if index >= len(self.message):
    #         return 1
        
    #     curr_message = self.message[index]
    #     if curr_message == '0':
    #         return 0

    #     result = self.decodeWays(index + 1)
    #     if index < len(self.message) - 1 and curr_message in {'1', '2'} and self.message[index + 1] in {'0', '1', '2', '3', '4', '5', '6'}:
    #             result += self.decodeWays(index + 2)

    #     return result
