'''
417. Pacific Atlantic Water Flow
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 
+-------------+
|  |  |  |  | |
+-------------+
|  |  |  |  | |
+-------------+
|  |  |  |  | |
+-------------+

Example 1:

Input: heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 
'''

from typing import List

# the key idea here is to start from borders that face atlantic and pacific.
# why?
# then do dfs on each of those cells.
# Basically, solver solves for atlantic and pacific seperately then 
# merge the 2 sets. 
# DFC adds a not to visited only if it have valid ht diff for water to flow.
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        result = []
        ROW, COL = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        for c in range(COL):
            self.canflow(0, c, heights, pacific, heights[0][c])
            self.canflow(ROW - 1, c, heights, atlantic, heights[ROW - 1][c])

        for r in range(ROW):
            self.canflow(r, 0, heights, pacific, heights[r][0])
            self.canflow(r, COL - 1, heights, atlantic, heights[r][COL - 1])

        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
    
    def canflow(self, r, c, heights, visited, prevht):
        rowvalid = 0 <= r < len(heights)
        colvalid = 0 <= c < len(heights[0])
        
        if not rowvalid or not colvalid:
            return 
        
        if (r,c) in visited:
            return

        # since these are the corners, hts should be smaller than the inner
        if heights[r][c] < prevht:
            return
        visited.add((r,c))
            
        self.canflow(r + 1, c, heights, visited, heights[r][c])
        self.canflow(r - 1, c, heights, visited, heights[r][c])
        self.canflow(r, c + 1, heights, visited, heights[r][c])
        self.canflow(r, c - 1, heights, visited, heights[r][c])
        return 
        
    
heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

s = Solution()
ans = s.pacificAtlantic(heights)
print("ans =", ans)
    