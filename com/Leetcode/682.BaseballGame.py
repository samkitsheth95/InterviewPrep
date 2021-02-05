from typing import List


class Solution:

    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)


sol = Solution()
print(sol.calPoints(ops=["5", "-2", "4", "C", "D", "9", "+", "+"]))
