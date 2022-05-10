from typing import List
from collections import deque


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        if rows == 1:
            return sum(grid[0])

        elif cols == 1:

            res = 0
            for row in grid:
                res += row[0]

            return res

        q = deque([(len(grid) - 2, len(grid[0]) - 1),
                  (len(grid) - 1, len(grid[0]) - 2)])

        visited = {(rows - 1, cols - 1), (rows - 2,
                                          cols - 1), (rows - 1, cols - 2)}

        while q:
            x, y = q.popleft()

            adjacent = [(x, y + 1), (x - 1, y), (x + 1, y), (x, y - 1)]

            minCost = float('inf')
            for r, c in adjacent:
                if 0 <= r < rows and 0 <= c < cols:

                    if (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))

                    elif grid[r][c] < minCost and (x - r + y - c < 0):
                        minCost = grid[r][c]

            grid[x][y] = grid[x][y] + minCost

        return grid[0][0]


Sol = Solution()
print(Sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
