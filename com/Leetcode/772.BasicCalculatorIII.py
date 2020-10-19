from collections import deque


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = deque()
        for i in s:
            if i != ' ':
                q.append(i)
        q.append('+')
        return self.helper(q)

    def helper(self, q):
        prevOp = '+'
        num, res, preSum = 0, 0, 0
        while q:
            i = q.popleft()
            if i.isdigit():
                num = 10 * num + int(i)
            elif i == '(':
                num = self.helper(q)
            else:
                if prevOp == '+':
                    res += preSum
                    preSum = num
                elif prevOp == '-':
                    res += preSum
                    preSum = -num
                elif prevOp == '*':
                    preSum *= num
                elif prevOp == '/':
                    temp = preSum
                    if temp // num < 0 and temp % num:
                        preSum = temp // num + 1
                    else:
                        preSum = temp // num
                if i == ')':
                    break
                num = 0
                prevOp = i
        return preSum + res


sol = Solution()
print(sol.calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
