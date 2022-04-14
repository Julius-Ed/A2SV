from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # west and east side
        for j in [0, cols - 1]:
            for i in range(rows):
                if grid[i][j] == 1:
                    # mark as visited by changing to - 1
                    grid[i][j] = -1
                    self.traverse((i, j), grid)

        # north and south side
        for i in [0, rows - 1]:
            for j in range(cols):
                if grid[i][j] == 1:
                    # mark as visited by changing to - 1
                    grid[i][j] = -1
                    self.traverse((i, j), grid)

        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += 1
        return res

    def traverse(self, cell, grid):
        rows, cols = len(grid), len(grid[0])
        dimensions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        q = deque([cell])

        while q:
            x, y = q.popleft()

            for dimension in dimensions:
                newX, newY = x + dimension[0], y + dimension[1]

                if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == 1:
                    grid[newX][newY] = -1
                    q.append((newX, newY))


Sol = Solution()

grid = [[0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]
print(Sol.numEnclaves(grid))
