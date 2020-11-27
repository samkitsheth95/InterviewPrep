from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits

    def plusOneNaive(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry > 9:
                temp = digits[i] + carry
                digits[i] = (temp) % 10
                carry = (temp) // 10
            else:
                digits[i] = digits[i] + carry
                carry = 0
                break
        if carry > 0:
            ans = [carry]
            ans.extend(digits)
            return ans
        return digits


sol = Solution()
print(sol.plusOne(digits=[9, 9, 9]))
