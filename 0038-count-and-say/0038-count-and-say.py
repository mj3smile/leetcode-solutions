class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(1, n):
            current_result = ""
            frequency = 0
            for c in range(len(result)):
                frequency += 1
                if (c < len(result) - 1 and result[c] != result[c + 1]) or c == len(result) - 1:
                    current_result += str(frequency) + str(result[c])
                    frequency = 0

            result = current_result
        
        return result