from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(len(triangle) - 2, - 1, -1):

            for j, val in enumerate(triangle[i]):
                triangle[i][j] = val + \
                    min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
Sol = Solution()
Sol.minimumTotal(triangle)

# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
