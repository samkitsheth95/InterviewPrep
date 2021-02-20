from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans, startTime, endTime = 0, 0, 0
        for time, prepTime in customers:
            endTime = (startTime if startTime > time else time) + prepTime
            ans += endTime - time
            startTime = endTime
        return ans / len(customers)


sol = Solution()
print(sol.averageWaitingTime(customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))
