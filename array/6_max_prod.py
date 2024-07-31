'''
6. Maximum Product Subarray
```
Given an integer array nums, find a subarray that has the largest
product, and return the product.
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''
from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        top = -sys.maxsize
        pre = 1
        post = 1

        rev = len(nums) -1
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            pre  *= nums[i]

            if post == 0:
                post = 1
            post *= nums[-i-1]

            if top < pre or top < post:
                top = pre if pre > post else post
        return top

    def maxProductBF(self, nums: List[int]) -> int:
        
        top = -sys.maxsize
        for val in range(len(nums)):
            product = 1
            for j in range(val, len(nums)):
                product *= nums[j]
            top = max(product, top)
        return top
    
"""
numss = [[2,3, 0, 2, 4, -2, 3,-3]]
ind num pos neg max
0   2   2   0
1   3   6   0   6
2   0   1   0   6
3   2   2   0   6
4   4   8   0   8
5  -2   8  -2  16
6   3   8  6   
7  -3   8  18  144
"""
s = Solution()
numss = []
numss +=  [[2,3, 0, -2, 4, -2, 3,-3]]
numss += [[2,3, 0, 2, 4, -2, 3,-3]]
numss += [[2,3,-2,4]]
numss += [[-2,0,-1]]
numss+= [[3,-1,4]]
for nums in numss:
    ans = s.maxProduct(nums)
    print("ans", ans, "for array", nums)