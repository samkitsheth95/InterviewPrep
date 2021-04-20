class Solution:

    def arrangeCoinsNaive(self, n: int) -> int:
        step, i = 0, 1
        while n > 0:
            n -= i
            if n >= 0:
                step += 1
            i += 1
        return step

    def arrangeCoinsBinarySearch(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = low + (high - low) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def arrangeCoinsMath(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)


sol = Solution()
print(sol.arrangeCoinsBinarySearch(5))
