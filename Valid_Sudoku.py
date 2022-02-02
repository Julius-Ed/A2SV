
class Solution:

    def isValidSudoku(self, board) -> bool:

        nonTransposeMatrix = self.check(board)
        transposeMatrix = self.check(self.transpose(board))

        if not nonTransposeMatrix or not transposeMatrix:
            return False

        quadtrants = [[0, 0], [0, 3], [0, 6],
                      [3, 0], [3, 3], [3, 6],
                      [6, 0], [6, 3], [6, 6]]

        for point in quadtrants:
            if not self.check_quadrants(board, point):
                return False

        return True

    # checks row for row for repeating numbers.
    def check(self, board) -> bool:

        for row in board:
            for index, ele in enumerate(row):
                if ele == ".":
                    continue
                if ele in row[index + 1:]:
                    return False

        return True

    # checks, given the upper-left cell of a 3*3 field, for repeating numbers.
    def check_quadrants(self, board, start):

        i, j = start

        set_of_values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        for row_index in range(i, i + 3):
            for column_index in range(j, j + 3):
                if board[row_index][column_index] == ".":
                    continue
                if board[row_index][column_index] not in set_of_values:
                    return False
                else:
                    set_of_values.remove(board[row_index][column_index])
        return True

    # transposes a the matrix.
    def transpose(self, board):

        transposed_matrix = []

        for i in range(len(board)):
            new_row = []
            for j in range(len(board)):
                new_row.append(board[j][i])
            transposed_matrix.append(new_row)

        return transposed_matrix
