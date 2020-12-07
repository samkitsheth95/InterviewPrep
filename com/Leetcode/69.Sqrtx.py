from math import e, log


class Solution:

    def mySqrtBinary(self, x: int) -> int:
        if x < 2:
            return x
        low = 2
        high = x // 2
        while low <= high:
            mid = low + (high - low) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def mySqrtPocketCalc(self, x):
        if x < 2:
            return x

        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right

    def mySqrtRecur(self, x):
        if x < 2:
            return x

        left = self.mySqrt(x >> 2) << 1
        right = left + 1
        return left if right * right > x else right

    def mySqrtNewton(self, x):
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)


sol = Solution()
print(sol.mySqrtNewton(4))
