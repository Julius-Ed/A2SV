from typing import List
from collections import deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        adjacencyList = {0: [[1, 1], 1]}

        for a, b in edges:
            if a not in adjacencyList:
                adjacencyList[a] = [[b], 1]
            else:
                adjacencyList[a][0].append(b)

            if b not in adjacencyList:
                adjacencyList[b] = [[a], 1]
            else:
                adjacencyList[b][0].append(a)
        


        if len(edges) == 0 and target == 1:
            return 1
        
        elif len(edges) == 0:
            return 0

        if target not in adjacencyList:
            return 0

        adjacencyList[1][0].append(0)
        

        #(current, level, parentNode)
        q = deque([(1, 0, 0)])
        visited = {0, 1}
        

        while q:

            curr, timeElapsed, parentNode = q.popleft()
            print(adjacencyList)

            # calculate propbabilty of curr
            # probCurr = probParen * (1 / numChildrenParen)

            probCurr = (1 / (len(adjacencyList[parentNode][0]) - 1)) * adjacencyList[parentNode][1]
            adjacencyList[curr][1] = probCurr

            if curr == target and timeElapsed <= t and len(adjacencyList[curr][0]) == 1:
                return probCurr
            
            elif curr == target and timeElapsed == t:
                return probCurr
            
            elif curr == target:
                return 0
            
            # add children to q

            for child in adjacencyList[curr][0]:
                if child in visited:
                    continue
                visited.add(child)
                q.append((child, timeElapsed + 1, curr))
        
        return  0



Sol = Solution()

# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 2
# target = 4


# n = 7
# edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
# t = 1
# target = 7


edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
n = len(edges)
t = 20
target = 6

print(Sol.frogPosition(n, edges, t, target))
        