"""
7. Find the Minimum in Rotated
```
Sorted Array
Given the sorted rotated array nums of unique elements, return
the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

[4,5,6,7,0,1,2]
[4,5,6, 7] [0,1,2] m=7, m > m+1 -> choose m+1 
           [0,1] [2]  m=1 m < m+1 - left 
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = [-1] * 1
        x = self.findMinHelper(nums, 0, len(nums) - 1, ans)
        return nums[ans[0]] if x is True else nums[0]
            
        

    def findMinHelper(self, nums, s, e, ans):
            
        if s >= e:
            return False
        
        m = s + (e - s)//2
        #print("s:",s, "e:", e, "m:", m)
        if nums[m] > nums[m+1]:
            ans[0] = m+1
            return True
        x = self.findMinHelper(nums, s, m, ans)
        if not x:
            x = self.findMinHelper(nums, m+1, e, ans)
        return x
            
        

s = Solution()
numss = []
numss += [[3,4,5,1,2]]
numss += [[4,5,6,7,0,1,2]]
numss += [[11,13,15,17]]
numss += [[3,1,2]]
for nums in numss:
    ans = s.findMin(nums)
    print("ans", ans)