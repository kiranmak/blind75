"""
11. Container With Most Water
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
0 1 2 3 4 5 6 7 8
1,8,6,2,5,4,8,3,7
^               ^
1=min(1,7)x(8-0) = 8
7=min(7,8)x( 8-1)=49
3        x (7-1) =18

pick next to smaller value -8
Example 2:
Input: height = [1,1]
Output: 1
 
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        if len(height) < 2:
            return 0
        
        max_area = 0
        curr_area = 0
        end = len(height) - 1
        start = 0
        while start < end:
            curr_area = min(height[start], height[end]) * (end - start)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            max_area = max(max_area, curr_area)
        return max_area

#height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
s = Solution()
ans = s.maxArea(height)
print("ans", ans)