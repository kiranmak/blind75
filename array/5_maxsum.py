"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
-2,1,-3,4, -1,
  -2, 1,
    
  -3,4,-1
   -3,   : -3
   4,-1   : 3
2,1,-5,4
   2,
     1, --
   -5,4

Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


 
"""
from typing import List
import sys

class Solution:
    global_top_sum = 0
    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane(nums)
    
    def kadane(self, nums):

        curr_sum = nums[0]
        top_sum = nums[0]
        
        for num in nums[1:]:

            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            top_sum = max(top_sum , curr_sum)

        return top_sum
         
    def maxSubArray2(self, nums: List[int]) -> int:
        self.global_top_sum = -sys.maxsize
        processed = []
        if len(nums) == 1:
            return nums[0]

        self.maxSubArrayHelper2(nums, 0, 0)
        return self.global_top_sum
    
    def maxSubArrayHelper2(self, nums, remain, curr_sum):
        if remain == len(nums):
            return 

        if curr_sum < 0:
            curr_sum = 0

        curr_sum += nums[remain]
        if self.global_top_sum < curr_sum:
            self.global_top_sum = curr_sum
         
        self.maxSubArrayHelper2(nums,remain +1, curr_sum)

    def maxSubArrayRec(self, nums: List[int]) -> int:
        self.global_top_sum = -sys.maxsize
        processed = []
        if len(nums) == 1:
            return nums[0]

        self.maxSubArrayHelper(processed, nums, 0)
        return self.global_top_sum
    
    def maxSubArrayHelper(self, start, remain, curr_sum):
        if len(remain) == 0:
            return 

        if curr_sum < 0:
            curr_sum = 0

        curr_sum += remain[0]
        self.global_top_sum = max(
            self.global_top_sum , curr_sum)
         
        self.maxSubArrayHelper(start + [remain[0]], remain[1:], curr_sum)

numss = [[-2,1,-3,4,-1,2,1,-5,4]]
numss += [[1]]
numss += [[-2,1]]
numss += [[-2,-1]]
numss += [[5,4,-1,7,8]]
s = Solution()
for nums in numss:
    ans = s.maxSubArray2(nums)
    print("ans:", ans, "arr:", nums)