class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
    
        for token in tokens:
            if len(token) > 1 and token[0] == "-":
                stack.append(int(token))
            elif token.isnumeric():
                stack.append(int(token))
            else:
                # Operator
                operand1 = stack.pop()
                operand2 = stack.pop()
                
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand2 - operand1)
                elif token == "/":
                    stack.append(int(operand2 / operand1))
                else:
                    stack.append(operand1 * operand2)
                    
        return stack[0]
        150. Evaluate Reverse Polish Notation
