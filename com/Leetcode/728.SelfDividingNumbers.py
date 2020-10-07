from typing import List


class Solution:

    def isValid(self, a):
        theNum = a
        while a > 0:
            temp = a % 10
            if not temp or theNum % temp:
                return False
            a = a // 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            if self.isValid(i):
                ans.append(i)
        return ans


sol = Solution()
print(sol.selfDividingNumbers(1, 22))
