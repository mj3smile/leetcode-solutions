class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        numbers = []
        
        first_num = ""
        i = 0
        while i < len(s) and s[i] not in {"+", "-", "*", "/"}:
            first_num += s[i]
            i += 1
        numbers.append(int(first_num))

        while i < len(s):
            operator = s[i]
            i += 1
            num_str = ""
            while i < len(s) and s[i] not in {"+", "-", "*", "/"}:
                num_str += s[i]
                i += 1
            
            num = int(num_str)
            if operator not in {"/", "*"}:
                numbers.append(num)
                operators.append(operator)
                continue
            
            if operator == "*":
                numbers[-1] = numbers[-1] * num
            else:
                numbers[-1] = numbers[-1] // num
        
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == "+":
                result += numbers[i + 1]
            else:
                result -= numbers[i + 1]
        return result