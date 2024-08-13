'''
128. Longest Consecutive Sequence
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
from typing import List

from numpy import sort


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_seq = 0
        for num in nums:
            if num - 1 not in numset:
                # start of seq
                count = 0
                while (num + count) in numset:
                    count += 1

            max_seq = max(max_seq, count)
        return max_seq
                
    def longestConsecutive2(self, nums: List[int]) -> int:
        seq = {}
        max_seq = 0
        numset = set(nums)
        for num in numset:
            left, right = 0, 0
            #is there something to left?
            if num - 1 in seq:
                left = seq[num - 1]

            if num + 1 in seq:
                right = seq[num + 1]

            seq_len = left + right + 1
            #seq[num] = seq_len
            seq[num - left] = seq_len
            seq[num + right] = seq_len
            #print("seq", seq)

            max_seq = max (max_seq, seq_len)
        return max_seq

nums = [100,4,200,1,3,2]
nums  = [1,2,0,1]
nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
s = Solution()
print("ans", s.longestConsecutive2(nums))
print("orig  =", nums)
print("sorted=", sort(nums))