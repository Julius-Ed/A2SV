
from collections import deque


def connectedCell(matrix):

    rows, cols = len(matrix), len(matrix[0])
    dimensions = [
        (-1, 1), (0, 1), (1, 1),
        (-1, 0), (1, 0),
        (-1, -1), (0, -1), (1, -1)
    ]

    res = 0

    while getFilledCell(matrix):
        i, j = getFilledCell(matrix)
        matrix[i][j] = 0
        currSize = 1

        q = deque([(i, j)])

        while q:

            i, j = q.popleft()

            res = max(res, currSize)
            currSize += 1

            for x, y in dimensions:
                iThetha = x + i
                jTheta = y + j

                if 0 <= iThetha < rows and 0 <= jTheta < cols and matrix[iThetha][jTheta] == 1:
                    q.append((iThetha, jTheta))
                    matrix[iThetha][jTheta] = 0

    return res


def getFilledCell(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                return i, j

    return None


grid = [[1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0]]
print(connectedCell(grid))
