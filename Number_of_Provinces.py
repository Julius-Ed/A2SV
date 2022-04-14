from typing import List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        cities = set()
        for i in range(len(isConnected)):
            cities.add(i)

        provinces = 0

        while len(cities) > 0:
            q = deque([cities.pop()])
            provinces += 1

            while q:
                city = q.popleft()

                for j in range(len(isConnected)):
                    if j in cities and isConnected[city][j] == 1:
                        cities.remove(j)
                        q.append(j)

        return provinces


isConnected = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]]

Sol = Solution()
print(Sol.findCircleNum(isConnected))
