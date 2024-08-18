'''
Given an integer array nums, return the length of the longest
strictly increasing subsequence.
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.
Input: nums = [0,1,0,3,2,3]
Output: 4.
'''
from typing import List
import sys

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    result = max(result, dp[i])
        
        return result
s = Solution()
nums = [0,1,0,3,2,3]
#nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums)) # --> 4