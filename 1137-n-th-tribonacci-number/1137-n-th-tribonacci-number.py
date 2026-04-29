class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        numbers = [0, 1, 1]
        result = 2
        for _ in range(3, n):
            numbers[0] = numbers[1]
            numbers[1] = numbers[2]
            numbers[2] = result
            result = sum(numbers)
        
        return result