"""
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 
1. You are given an array prerequisites where
 prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

approach: looks like a graph cycle problem - how to find cycle.
- first create a an adjList from course pairs.
- follow chain of course that can finish.
- A course with no outward edge is not dependent, i.e. has empty adjlist.
- empty adjList means course can complete

"""
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjList = self.makeGraph(numCourses, prerequisites)
        adjList = {i:[] for i in range(numCourses)}
        for f,s in prerequisites:
            adjList.get(f).append(s)

        visited = set()
        for course in range(numCourses):
            if not self.dfs(course, adjList, visited):
                return False
        return True    

    def makeGraph(self, n, prereqs):
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in prereqs:
            f, s = edge[0], edge[1]
            adj.get(f).append(s)
        return adj

    def dfs(self, course, adjList, visited):

        if course in visited:
            return False

        if adjList.get(course) == []:
            return True

        print(course, end="")
        visited.add(course)

        for other in adjList[course]:
            res = self.dfs(other, adjList, visited)
            if not res: return False
        visited.remove(course)

        adjList[course] = []
        return True

    def show(self, numCourses: int, prerequisites: List[List[int]]):
        adjList = {i:[] for i in range(numCourses)}
        for f,s in prerequisites:
            adjList.get(f).append(s)

        for course in range(numCourses):
            visited = set()
            self.dfsshow(course, adjList, visited)
            print(".")

    def dfsshow(self, course, adjList, visited):

        if course in visited:
            return

        print(course, "->", end="")
        visited.add(course)

        for other in adjList[course]:
            self.dfsshow(other, adjList, visited)
        visited.remove(course)

        adjList[course] = []

s = Solution()
edges = [[0,1], [0,2], [1,3],[1,4],[3,4]]
#edges = [[0,1], [1,0]]
#ans = s.canFinish(5, edges)
ans = s.show(5, edges)
print("ans for scedule is", ans)
