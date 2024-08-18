'''
57. Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals is []:
            return []
        
        left, right = [], []
        start, end = newInterval

        for st, en in intervals:
            if en < start:
                left.append([st,en])
                #print("go left:", [start, end], "with", [st,en])
            elif st > end:
                #print("go right:", [start, end], "with", [st,en])
                right.append([st,en])
            else:
                #print("overlap:", [start, end], "with", [st,en])
                [start, end] = [min(start, st), max(end, en)]

        return left + [[start, end]] + right

s1 = Solution()
print(s1.insert([[1,3],[6,9]], [2,5])) # --> [1,5], [6,9]
            
print(s1.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) #=> [[1,2],[3,10],[12,16]]