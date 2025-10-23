class Solution:
    def countBits(self, n: int) -> List[int]:
        result = list()
        previous_power_of_two = 0

        for i in range(n + 1):
            if i == 0:
                result.append(0)
            elif self.isPowerOfTwo(i):
                previous_power_of_two = i
                result.append(1)
            else:
                result.append(result[i - previous_power_of_two] + result[previous_power_of_two])
        return result

    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0
    
    # def countOneBit(self, n):
    #     result = 0
    #     while n > 0:
    #         if n & 1 == 1:
    #             result += 1
    #         n = n // 2
    #     return result