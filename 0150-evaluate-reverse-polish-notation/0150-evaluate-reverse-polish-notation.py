class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = list()
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                numbers.append(int(t))
                continue
            
            number2 = numbers.pop()
            number1 = numbers.pop()
            print(number1, t, number2)
            if t == "+":
                numbers.append(number1 + number2)
            elif t == "-":
                numbers.append(number1 - number2)
            elif t == "*":
                numbers.append(number1 * number2)
            else:
                sign = 1
                if (number1 < 0 and number2 >= 0) or (number1 >= 0 and number2 < 0):
                    sign = -1
                if number1 < 0:
                    number1 *= -1
                if number2 < 0:
                    number2 *= -1

                numbers.append(number1 // number2 * sign)
        
        return numbers[0]