'''
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
import heapq
from typing import List
from heapq import _heappop_max,heappush

class MyDict:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other): return self.value < other.value
    def __gt__(self, other): return self.value > other.value
    def __eq__(self, other): return self.value == other.value
    def __repr__(self):
        return f'(k={self.key!r}, v={self.value})'

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        mydict = {}
        result = []
        for val in nums:
            mydict[val] = mydict.get(val, 0) + 1
        
        heap =[]
        for key in mydict:
            item = MyDict(key, -1 * mydict[key])
            heappush(heap, item)
        for i in range(k):
            item = heapq.heappop(heap)
            result.append(item.key)
        return result

#nums, k = [4,4,4,9,9,6], 2
nums, k = [1], 1
nums, k = [4,1,-1,2,-1,2,3], 2
s = Solution()
ans = s.topKFrequent(nums, k)
print("ans", ans)