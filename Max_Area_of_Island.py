from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0

        dimensions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        # loop over all cells in the grid.
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 0:
                    continue

                q = deque([(i, j)])

                islandSize, grid[i][j] = 0, 0

                # if a cell is an island, run bfs on it and track island size.
                while q:

                    x, y = q.popleft()

                    islandSize += 1
                    res = max(res, islandSize)

                    # create neighbouring cells.
                    for dimension in dimensions:
                        newX, newY = x + dimension[0], y + dimension[1]

                        # only add them to the que if they are islands themselves.
                        if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == 1:
                            q.append((newX, newY))

                            # mark islands as visited by turning them to 0.
                            grid[newX][newY] = 0

        return res


Sol = Solution()


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]


print(Sol.maxAreaOfIsland(grid))
