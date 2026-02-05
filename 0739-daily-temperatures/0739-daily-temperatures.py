class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        stack = list()
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                pastTemp, index = stack.pop()
                result[index] = i - index
            stack.append((temperatures[i], i))
        return result