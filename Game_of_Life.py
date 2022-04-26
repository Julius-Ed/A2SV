from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        for x in range(rows):
            for y in range(cols):

                newState = self.changeState(board, (x, y))
                if newState:
                    board[x][y] = newState

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 2:
                    board[x][y] = 0
                if board[x][y] == 3:
                    board[x][y] = 1

    def getEightNeighbours(self, board, parent):

        a, b = parent

        dimensions = [
            (-1, 1,), (0, 1), (1, 1),
            (-1, 0), (1, 0),
            (-1, -1), (0, -1), (1, -1)
        ]

        neighs = []

        for x, y in dimensions:

            c = x + a
            d = y + b

            if 0 <= c < len(board) and 0 <= d < len(board[0]):
                neighs.append((c, d))

        return neighs

    def changeState(self, board, parent):

        neighs = self.getEightNeighbours(board, parent)

        livingNeighs = 0
        for x, y in neighs:
            if board[x][y] == 1 or board[x][y] == 2:
                livingNeighs += 1

        # 3: cell has been dead and lives now.
        # 2: cell was alive and is now dead.

        # was dead and is turned alive now since has 3 living neighs.
        if (board[parent[0]][parent[1]] == 0 or board[parent[0]][parent[1]] == 3) and livingNeighs == 3:
            # return 1
            return 3

        # otherwise, dead cells stay dead.
        elif board[parent[0]][parent[1]] == 0:
            # return 0
            return None

        # cell was alive and is turned dead now.
        if livingNeighs <= 1:
            # return 0
            return 2

        # cell was alive and is turned dead now
        if livingNeighs >= 4:
            # return 0
            return 2

        # otherwise cells continue to be alive
        # return 1
        return None


Sol = Solution()


"""
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]


Sol.gameOfLife(board)
print(" ")
for e in expected:
    print(e)
