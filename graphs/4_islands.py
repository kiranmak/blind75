'''
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
 
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        row, col = len(grid), len(grid[0])
        count = 0
            
        for r in range(row):
            for c in range(col):
                if self.explore(grid, r, c):
                    count += 1
        return count 
    
    def explore(self, grid, r, c):

        if r < 0 or r >= len(grid):
            return False
            
        if c < 0 or  c >= len(grid[0]):
            return False

        if grid[r][c] == "0":
            return  False

        grid[r][c] = "0"
        self.explore(grid, r, c + 1)
        self.explore(grid, r, c - 1)
        self.explore(grid, r + 1, c)
        self.explore(grid, r - 1, c)
        
        return  True

    def explore2(self, grid, r, c, vis):

        if r < 0 or r >= len(grid):
            return False
            
        if c < 0 or  c >= len(grid[0]):
            return False

        if grid[r][c] == "0":
            return  False

        grid[r][c] = "0"
        self.explore(grid, r, c + 1, vis)
        self.explore(grid, r, c - 1, vis)
        self.explore(grid, r + 1, c, vis)
        self.explore(grid, r - 1, c, vis)
        
        return  True

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid2 = [
  ['0', '1', '0', '0', '0'],
  ['0', '1', '0', '0', '0'],
  ['0', '0', '0', '1', '0'],
  ['0', '0', '1', '1', '0'],
  ['1', '0', '0', '1', '1'],
  ['1', '1', '0', '0', '0'],
]

grid3 = [
  ['0', '1', '0'],
  ['1', '1', '0'],
  ['0', '1', '1'],
  ['0', '0', '0'],
    
]
grid4 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = Solution()
inputs = [grid, grid1, grid2, grid3, grid4]
for gr in inputs:
    for ar in gr:
        print(ar)
    count = s.numIslands(gr)
    print("output = ", count)