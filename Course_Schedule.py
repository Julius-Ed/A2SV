from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjacencyList = {}
        inbound = {}

        # create empty adjacency and inbound maps.
        for i in range(numCourses):
            inbound[i] = 0
            adjacencyList[i] = []

        # populate adjacency list
        for a, b in prerequisites:
            adjacencyList[a].append(b)

        # count inbounds
        for _, b in prerequisites:
            inbound[b] += 1

        q = deque([])
        # start with those nodes that don't have inbounds
        for course in inbound:
            if inbound[course] == 0:
                q.append(course)

        res = []
        while q:

            currCourses = q.popleft()
            res.append(currCourses)

            # check whether a loop exists
            if len(res) > numCourses:
                return False

            children = adjacencyList[currCourses]

            # decrease inbounds for children since we removed a node.
            for child in children:
                inbound[child] -= 1

                # nodes without inbounds can be appended to the que.
                if inbound[child] == 0:
                    q.append(child)

        return len(res) == numCourses


numCourses = 5
prerequisites = [
    [0, 1],
    [1, 0],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 4]
]
Sol = Solution()
print(Sol.canFinish(numCourses, prerequisites))
