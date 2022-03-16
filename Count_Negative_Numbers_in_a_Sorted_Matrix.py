from itertools import count
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        row, col, res = rows - 1, 0, 0

        while row >= 0 and col < cols:
            if grid[row][col] <= -1:
                res += cols - col
                row -= 1
            else:
                col += 1

        return res


Sol = Solution()
print(Sol.countNegatives(
    [[4, 3, 2, -1],
     [3, 2, 1, -1],
     [1, 1, -1, -2],
     [-1, -1, -2, -3]]
))
