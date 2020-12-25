from typing import List


class Solution(object):

    def dailyTemperaturesUsingTempRange(self, T: List[int]) -> List[int]:
        temp = [31000] * 102
        n = len(T)
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            nextWarmer = min(temp[j] for j in range(T[i] + 1, 102))
            if nextWarmer != 31000:
                ans[i] = nextWarmer - i
            temp[T[i]] = i

        return ans

    def dailyTemperaturesSmart(self, T):
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

    def dailyTemperaturesLeetcodeSol(self, T):
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


sol = Solution()
print(sol.dailyTemperaturesUsingTempRange([73, 74, 75, 71, 69, 72, 76, 73]))
