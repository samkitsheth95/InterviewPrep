from typing import List


class Solution:

    def mergeNormal(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ans.append(intervals[0])
        prevEnd = intervals[0][1]
        for start, end in intervals:
            if start <= prevEnd:
                if end > prevEnd:
                    ans[-1][1] = end
                    prevEnd = end
            else:
                ans.append([start, end])
                prevEnd = end
        return ans

    def merge(self, intervals):
        ans = []
        for start, end in sorted(intervals):
            if not ans or ans[-1][1] < start:
                ans += [[start, end]]
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans


sol = Solution()
print(sol.mergeNormal(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
