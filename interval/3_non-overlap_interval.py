
'''
435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals is []:
            return []
        
        # this is the key. intuition: by sorting on end times, we get more intervals with shorter time.
        def sortkey(e):
            return e[1]
        
        intervals.sort(key=sortkey)
        count = 1 
        i = 1
        last = 0
        while i < len(intervals):
            # non-overlapping
            if intervals[i][0] >= intervals[last][1]:
                count += 1
                last = i
            i +=1

        return (len(intervals) - count)

s1 = Solution()
# intervals = [[1,2],[2,3],[3,4],[1,3]]
# print(s1.eraseOverlapIntervals(intervals)) # --> 1
# intervals = [[1,2],[1,2],[1,2]]
# print(s1.eraseOverlapIntervals(intervals)) # --> 2
# intervals = [[1,2],[2,3],[3,6]]
# print(s1.eraseOverlapIntervals(intervals)) # --> 0

#intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49], [-31, 49]]
#[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(s1.eraseOverlapIntervals(intervals)) # --> 3