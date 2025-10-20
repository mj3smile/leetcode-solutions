class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number_presence = list()

        for n in nums:
            if n + 1 > len(number_presence):
                for _ in range(n + 1 - len(number_presence)):
                    number_presence.append(-1)

            number_presence[n] = 0

        result = len(number_presence)
        for i in range(len(number_presence)):
            if number_presence[i] == -1:
                return i

        return result 