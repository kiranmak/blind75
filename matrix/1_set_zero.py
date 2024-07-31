"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_sz, col_sz = len(matrix), len(matrix[0])
        mark_row = [False] * row_sz
        mark_col = [False] * col_sz
        
        for row in range(row_sz):
            for col in range(col_sz):
                if matrix[row][col] == 0:
                    mark_col[col] = True
                    mark_row[row] = True

        for r in range(row_sz):
            if mark_row[r]:
                matrix[r] = [0] * col_sz

        for c in range(col_sz):
            if mark_col[c]:
                for r in range(row_sz):
                    matrix[r][c] = 0


#matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(matrix)
s = Solution()
s.setZeroes(matrix)
print(matrix)
