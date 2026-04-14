class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if v not in ['*', '+', '-', '/']:
                stack.append(int(v))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                if v == '+':
                    res = v1 + v2
                elif v == '-':
                    res = v2 - v1
                elif v == '*':
                    res = v1 * v2
                else:
                    res = v2 / v1
                stack.append(int(res))

        return stack[-1]
