"""
1. Two Sum
Given an array of integer nums and an integer target, return
indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] +nums[1] == 9, we return [0, 1].
(https://leetcode.com/problems/two-sum/) 
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        for i in range(len(nums)):
            if (target - nums[i]) in remaining:
                return [remaining[target - nums[i]], i]
            else:
                remaining[nums[i]] = i

s = Solution()
#nums = [2,7,11,15]  # target = 9
nums = [3,2,4]  # target = 6
nums = [3,3]  # target = 6
ans = s.twoSum(nums, 6)
print(ans)
   