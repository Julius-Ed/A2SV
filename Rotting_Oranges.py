from typing import List
from collections import deque


"""
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # collect rotten oranges.
        rottenStart = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rottenStart.append((row, col, 0))

        q = deque(rottenStart)

        fourDimensions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        res = 0

        while q:

            row, col, mins = q.popleft()
            res = max(res, mins)

            for dimension in fourDimensions:
                x, y = dimension

                candidate = (row + y, col + x, mins + 1)

                if 0 <= candidate[0] < rows and 0 <= candidate[1] < cols and grid[candidate[0]][candidate[1]] == 1:
                    grid[candidate[0]][candidate[1]] = 2
                    q.append(candidate)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return - 1

        return res


Sol = Solution()
print(Sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
