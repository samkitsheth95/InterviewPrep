from typing import List
from collections import defaultdict, deque


class node:
    def __init__(self):
        self.degree = 0
        self.dependentCourses = []


class Solution:

    def isCycle(self, course, courseInfo, prereqmap):
        if courseInfo[course] == 1:
            return True
        courseInfo[course] = 1
        if course in prereqmap:
            for preReq in prereqmap[course]:
                if courseInfo[preReq] == 2:
                    continue
                if self.isCycle(preReq, courseInfo, prereqmap):
                    return True
        courseInfo[course] = 2
        return False

    def canFinishAdjacencyMatrix(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqmap, courseInfo = defaultdict(list), [0] * numCourses

        for course, preReq in prerequisites:
            prereqmap[course].append(preReq)

        for course in prereqmap.keys():
            if self.isCycle(course, courseInfo, prereqmap):
                return False
        return True

    def canFinishTopologicalSort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, takenCourses = [], 0

        for _ in range(numCourses):
            graph.append(node())

        for course, prereq in prerequisites:
            graph[prereq].dependentCourses.append(course)
            graph[course].degree += 1

        q = deque()

        for course in range(numCourses):
            if graph[course].degree == 0:
                q.append(course)

        while q:
            noPrereqCourse = q.popleft()
            takenCourses += 1
            for course in graph[noPrereqCourse].dependentCourses:
                graph[course].degree -= 1

                if graph[course].degree == 0:
                    q.append(course)

        return takenCourses == numCourses


sol = Solution()
print(sol.canFinishTopologicalSort(numCourses=5, prerequisites=[
      [1, 4], [2, 4], [3, 1], [3, 2]]))
