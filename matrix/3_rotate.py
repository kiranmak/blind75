"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                #rotate in reverse
                save = matrix[top][l + i]
                matrix[top ][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = save
            l +=1
            r -=1
            

#matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix=[[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]
s = Solution()
for m in matrix:
    print(m)
s.rotate(matrix)
print("right rotate")
for m in matrix:
    print(m)
