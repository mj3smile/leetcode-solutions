class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            item = str(i)
            if i % 15 == 0:
                item = "FizzBuzz"
            elif i % 3 == 0:
                item = "Fizz"
            elif i % 5 == 0:
                item = "Buzz"
            
            result.append(item)
        
        return result
                