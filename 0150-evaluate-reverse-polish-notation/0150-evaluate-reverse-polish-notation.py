class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = list()
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operators:
                numbers.append(int(t))
                continue
            
            second_num = numbers.pop()
            first_num = numbers.pop()

            if t == "+":
                numbers.append(first_num + second_num)
            elif t == "-":
                numbers.append(first_num - second_num)
            elif t == "*":
                numbers.append(first_num * second_num)
            else:
                numbers.append(int(first_num / second_num))
            
        return numbers[0]