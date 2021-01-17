from typing import List


class Solution:
    def maximumWealthOne(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            ans = max(ans, sum(i))
        return ans

    def maximumWealthTwo(self, accounts):
        return max(map(sum, accounts))


sol = Solution()
print(sol.maximumWealthOne(accounts=[[1, 2, 3], [3, 2, 1]]))
