from collections import defaultdict
from typing import List


class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i + j].append(nums[i][j])
        for i in d.values():
            i.reverse()
            ans.extend(i)
        return ans


sol = Solution()
print(sol.findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [
      6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
