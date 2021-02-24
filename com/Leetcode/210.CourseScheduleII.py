from typing import List
from collections import defaultdict, deque


class node:
    def __init__(self):
        self.degree = 0
        self.dependentCourses = []


class Solution:

    def findOrderTopo(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, ans = [], []

        for _ in range(numCourses):
            graph.append(node())

        for course, prereq in prerequisites:
            graph[prereq].dependentCourses.append(course)
            graph[course].degree += 1

        q = deque()

        for course in range(numCourses):
            if graph[course].degree == 0:
                q.append(course)
                ans.append(course)

        while q:
            noPrereqCourse = q.popleft()

            for course in graph[noPrereqCourse].dependentCourses:
                graph[course].degree -= 1

                if graph[course].degree == 0:
                    q.append(course)
                    ans.append(course)

        return ans if len(ans) == numCourses else []

    def isCycle(self, course, courseInfo, prereqmap, ans):
        if courseInfo[course] == 1:
            return True
        if courseInfo[course] == 2:
            return False

        courseInfo[course] = 1
        if course in prereqmap:
            for preReq in prereqmap[course]:
                if courseInfo[preReq] == 2:
                    continue
                if self.isCycle(preReq, courseInfo, prereqmap, ans):
                    return True
        courseInfo[course] = 2
        ans.append(course)
        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqmap, courseInfo = defaultdict(list), [0] * numCourses
        ans = []
        for course, preReq in prerequisites:
            prereqmap[course].append(preReq)
        for course in range(numCourses):
            if self.isCycle(course, courseInfo, prereqmap, ans):
                return []
        return ans


sol = Solution()
print(sol.findOrderTopo(numCourses=4, prerequisites=[
      [1, 0], [2, 0], [3, 1], [3, 2]]))
