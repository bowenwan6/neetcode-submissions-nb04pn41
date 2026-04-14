class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            # If it's a number, push it as an integer
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                # Pop the last two values
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:  # token == "/"
                    # Integer division that truncates toward zero
                    result = int(a / b)
                
                # Push the computed result back onto the stack
                stack.append(result)
        
        # The final answer is the single value left on the stack
        return stack.pop()
