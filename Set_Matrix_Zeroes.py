from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        zeroColumn = False

        for row in range(rows):
            for column in range(columns):

                if matrix[row][column] == 0:
                    if column != 0:
                        matrix[0][column] = 0
                    else:
                        zeroColumn = True

                    matrix[row][0] = 0

        for column in range(1, columns):
             if matrix[0][column] == 0:

                 for row in range(rows):
                     matrix[row][column] = 0
    

        for row in range(rows):
            if matrix[row][0] == 0:

                for column in range(columns):
                    matrix[row][column] = 0
    
        if zeroColumn:
            for row in range(rows):
                matrix[row][0] = 0




Sol = Solution()
Sol.setZeroes( [[1,1,1],
               [1,0,1],
                [1,1,1]])

Sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])