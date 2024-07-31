"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[I].
The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.
You must write an algorithm that runs in O(n) time and without
using the division operation.
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
       pre suf prod
0  2   1 60    60
1  3   2 20    40
2  4   6  5    30
3  5  24  1    24
"""

from typing import List
import sys

class Solution:
    def maxProductExceptSelf(self, nums: List[int]) -> int:
        
        print("idx val pre, suf")
        product = [1] * len(nums)
        pre  = [1] * len(nums)
        suff = [1] *len(nums)
        pre[0] = 1
        suff[-1] = 1 
        print("i  nums[i] pre[i]  suff[i]")
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
            suff[-i-1] = suff[-i] * nums[-i]

        #for i in range(len(nums)-2, -1, -1):

        for i in range(len(nums)):
            print(f"{i}   {nums[i]}   {pre[i]}   {suff[i]}")
             
        for i in range(len(nums)):
            product[i] = pre[i] * suff[i] 
        return product

s = Solution()
#numss =  [[2,3, 0, -2, 4, -2, 3,-3]]
#numss += [[2,3, 0, 2, 4, -2, 3,-3]]
#numss += [[2,3,-2,4]]
#numss += [[-2,0,-1]]
#numss+= [[3,-1,4]]
numss = [[ 2, 3, 4, 5]]
for nums in numss:
    ans = s.maxProductExceptSelf(nums)
    print("ans", ans)