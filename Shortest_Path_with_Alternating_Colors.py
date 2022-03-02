from collections import deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        res = [-1] * n

        reds, blues = {}, {}

        for i in range(n):
            reds[i] = []
            blues[i] = []

        for red in redEdges:
            reds[red[0]].append(red[1])

        for blue in blueEdges:
            blues[blue[0]].append(blue[1])

        for prev in ["red", "blue"]:

            visited = {
                "blue": set(),
                "red": set()}

            level = 0
            q = deque([(0, 0)])

            while q:
                current, level = q.popleft()

                if level < res[current] or res[current] == -1:
                    res[current] = level

                if prev == "red":
                    visited["red"].add(current)
                    children = blues[current]

                    for child in children:
                        if child not in visited["blue"]:
                            q.append((child, level + 1))

                    prev = "blue"

                else:
                    visited["blue"].add(current)
                    children = reds[current]

                    for child in children:
                        if child not in visited["red"]:
                            q.append((child, level + 1))

                    prev = "red"

        return res


Sol = Solution()
#print(Sol.shortestAlternatingPaths(3, [[0, 1], [2, 1]], []))
#print(Sol.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]))
#print(Sol.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))
print(Sol.shortestAlternatingPaths(5, [[2, 2], [0, 1], [0, 3], [0, 0], [0, 4], [
      2, 1], [2, 0], [1, 4], [3, 4]], [[1, 3], [0, 0], [0, 3], [4, 2], [1, 0]]) == [0, 1, 2, 1, 1])
