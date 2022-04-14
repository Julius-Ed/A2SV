from collections import deque
from typing import List

from regex import P


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Any 'O' that is not on the border and it is not connected to an 'O' on the 
        border will be flipped to 'X'
        """
        dimensions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        rows, cols = len(board), len(board[0])

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):

                if board[row][col] != "O":
                    continue

                q = deque([(row, col)])
                group, bordering = [(row, col)], False
                visited = set((row, col))

                while q:
                    x, y = q.popleft()

                    if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
                        bordering = True

                    for dimension in dimensions:
                        newX, newY = x + dimension[0], y + dimension[1]

                        # only add them to the que if they are islands themselves.
                        if (newX, newY) not in visited and 0 <= newX < rows and 0 <= newY < cols and board[newX][newY] == "O":
                            q.append((newX, newY))
                            group.append((newX, newY))
                            visited.add((newX, newY))

                if not bordering:
                    for i, j in group:
                        board[i][j] = "X"


Sol = Solution()


board = [["X", "X", "X"],
         ["X", "O", "X"],
         ["X", "X", "X"]]

Sol.solve(board)
