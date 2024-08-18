'''
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from typing import List


class Solution:
    #def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x:  x[1])
        print(intervals)
        
        prevFinish = intervals[0][1]
        for meet in intervals[1:]:
            if prevFinish > meet[0]:
                return False
            prevFinish = meet[1]
        return True
                
s = Solution()
intervals = [[0,30],[5,10],[15,20]]
print(intervals)
print(s.canAttendMeetings(intervals)) # --> False
intervals = [[7,10],[2,4]]
print(s.canAttendMeetings(intervals)) # --> True