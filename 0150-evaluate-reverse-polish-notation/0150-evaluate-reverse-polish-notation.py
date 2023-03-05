class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers  = []
        
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                numbers.append(int(t))
                continue
            
            second = numbers.pop()
            first = numbers.pop()
            result = 0
            
            if t == '+':
                result = first + second
            elif t == '-':
                result = first - second
            elif t == '*':
                result = first * second
            else:
                result = int(first / second)
            
            numbers.append(result)
        
        return numbers[0]