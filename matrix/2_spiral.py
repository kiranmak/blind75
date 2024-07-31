"""
54. Spiral Matrix
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral = []
        rend, cend = len(matrix) , len(matrix[0])
        rst, cst = 0,0
        while cst < cend and rst < rend:
            print(f"1. rst={rst}, cst={cst}, rend={rend}, cend={cend}")
            for i in range(cst, cend):
                spiral.append(matrix[rst][i])
            rst += 1
            print(f"2. rst={rst}, cst={cst}, rend={rend}, cend={cend}")
            for i in range(rst, rend):
                spiral.append(matrix[i][cend - 1])
            cend -= 1 
            
            print(f"3. rst={rst}, cst={cst}, rend={rend}, cend={cend}")
            if rend > rst:
                for i in range(cend-1, cst-1, -1):
                    spiral.append(matrix[rend - 1][i])
                rend -=1
            if cend > cst:
                for i in range(rend-1, rst-1, -1):
                    spiral.append(matrix[i][cst])
                cst += 1
            print(f"4. rst={rst}, cst={cst}, rend={rend}, cend={cend}")
        return spiral

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
matrix = [[6,9,7]]

print(matrix)
s = Solution()
spiral = s.spiralOrder(matrix)
print(spiral)

        