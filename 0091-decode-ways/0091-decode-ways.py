class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
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
