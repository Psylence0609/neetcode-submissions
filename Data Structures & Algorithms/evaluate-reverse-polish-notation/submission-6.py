class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        # loop through tokens
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    div = num1 // num2
                    if num1 % num2 != 0 and div < 0:
                        div += 1
                    stack.append(div)
                        
                print(stack)
                print(token)
        return stack[0]