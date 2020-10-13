class Solution:
    def cc(self, a, b, x):
        if x == '+':
            return a + b
        elif x == '-':
            return a - b
        elif x == '*':
            return a * b
        else:
            if a // b < 0 and a % b:
                return a // b + 1
            else:
                return a // b

    def calculateNaive(self, s: str) -> int:
        stack = []
        current = 0
        prevOp = '+'
        for i in s:
            if i.isdigit():
                current = 10 * current + int(i)
            elif i == '+' or i == '-':
                if len(stack) and (stack[-1] == '*' or stack[-1] == '/'):
                    op = stack.pop()
                    stack.append(self.cc(stack.pop(), current, op))
                else:
                    stack.append(-current if prevOp == '-' else current)
                stack.append('+')
                current = 0
                prevOp = '-' if i == '-' else '+'
            elif i == '*' or i == '/':
                if len(stack) and (stack[-1] == '*' or stack[-1] == '/'):
                    op = stack.pop()
                    stack.append(self.cc(stack.pop(), current, op))
                else:
                    stack.append(-current if prevOp == '-' else current)
                stack.append('*' if i == '*' else '/')
                current = 0
                prevOp = '*' if i == '*' else '/'
        stack.append(-current if prevOp == '-' else current)
        while len(stack) > 1:
            b = stack.pop()
            op = stack.pop()
            a = stack.pop()
            stack.append(self.cc(a, b, op))
        return stack[0]

    def calculate(self, s: str) -> int:
        s += '+'
        stack = []
        num = 0
        prevOp = '+'
        for i in s:
            if i.isdigit():
                num = 10 * num + int(i)
            elif not i == ' ':
                if prevOp == '+':
                    stack.append(num)
                elif prevOp == '-':
                    stack.append(-num)
                elif prevOp == '*':
                    stack.append(stack.pop() * num)
                elif prevOp == '/':
                    temp = stack.pop()
                    if temp // num < 0 and temp % num:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                num = 0
                prevOp = i
        return sum(stack)


sol = Solution()
print(sol.calculate("3+2*2"))
