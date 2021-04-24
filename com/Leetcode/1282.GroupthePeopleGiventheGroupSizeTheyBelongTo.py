from collections import defaultdict
from typing import List

class Solution:

    def groupThePeopleArr(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        tempAns = [[] for _ in range(n + 1)]
        ans = []
        for i in range(n):
            tempAns[groupSizes[i]].append(i)
            if len(tempAns[groupSizes[i]]) == groupSizes[i]:
                ans.append(tempAns[groupSizes[i]])
                tempAns[groupSizes[i]] = []
        return ans

    def groupThePeopleDict(self, groupSizes: List[int]) -> List[List[int]]:
        sizeToGroup, res = defaultdict(list), []
        for i, size in enumerate(groupSizes):
            sizeToGroup[size].append(i)
            if len(sizeToGroup[size]) == size:
                res.append(sizeToGroup.pop(size))
        return res


sol = Solution()
print(sol.groupThePeopleDict(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
