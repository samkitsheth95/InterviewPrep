from typing import List


class Solution:
    def helper(self, a, b, i):
        if i == '/':
            return int(a/b)
        if i == '-':
            return a - b
        if i == '*':
            return a * b
        else:
            return a + b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "/*+-":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.helper(a, b, i))
            else:
                stack.append(int(i))
        return stack[0]

    def evalRPNLambda(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        for i in tokens:
            if i in "/*+-":
                b = stack.pop()
                a = stack.pop()
                operation = operations[i]
                stack.append(operation(a, b))
            else:
                stack.append(int(i))
        return int(stack[0])


sol = Solution()
print(sol.evalRPN(["10", "6", "9", "3", "+",
                         "-11", "*", "/", "*", "17", "+", "5", "+"]))
