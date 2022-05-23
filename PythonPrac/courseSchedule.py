"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.
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
To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.
"""
def canFinish(numCourse: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(numCourse)]
    visit = [0 for _ in range(numCourse)]
    canTake = [False for _ in range(numCourse)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i, canTake):
        if canTake[i]:
            return True
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j, canTake):
                return False
        visit[i] = 1
        return True
    for i in range(numCourse):
        if not dfs(i, canTake):
            return False
        else:
            canTake[i] = True
    return True

print(canFinish(5, [[4,3], [4,2], [4,1], [4,0], [3, 2], [2, 1]]))
print(canFinish(2, [[1,0], [0,1]]))
print(canFinish(2, [[1,0]]))
