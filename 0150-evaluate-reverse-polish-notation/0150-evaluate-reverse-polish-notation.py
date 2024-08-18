class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        operator = tokens.pop()
        if operator not in operators:
            return int(operator)
        
        operand2 = int(tokens.pop()) if tokens[-1] not in operators else self.evalRPN(tokens)
        operand1 = int(tokens.pop()) if tokens[-1] not in operators else self.evalRPN(tokens)
        
        return self.calculate(operand1, operand2, operator)
                
        
    def calculate(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return int(operand1 / operand2)
