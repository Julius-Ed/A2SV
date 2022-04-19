from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        initColor = image[sr][sc]

        dimensions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q, seen = deque([(sr, sc)]), set()
        image[sr][sc] = newColor

        while q:

            x, y = q.popleft()
            seen.add((x, y))

            for dim in dimensions:
                xTheta, yTheta = dim

                xChild, yChild = x + xTheta, y + yTheta

                if (xChild, yChild) not in seen and 0 <= xChild < rows and 0 <= yChild < cols and image[xChild][yChild] == initColor:
                    image[xChild][yChild] = newColor
                    q.append((xChild, yChild))

        return image


Sol = Solution()
res = Sol.floodFill(
    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2
)


for row in res:
    print(row)
