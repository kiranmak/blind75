'''
Meeting Schedule II
Given an array of meeting time intervals consisting of start and
end times[[s1,e1],[s2,e2],...](si< ei).
Find the minimum number of conference rooms required.
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1


Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)
Example 2:
Input: intervals = [(4,9)]
Output: 1
Note: (0,8),(8,10) is not considered a conflict at 8
Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''

#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
def addInterval( items):
    intervals = []
    for item in items:
        intervals.append(Interval(item[0], item[1]))
    return intervals

from typing import List

# intuition: number of ongoing meetings. create a sorted timeline
# by flattening start end times in one array

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        
        sched = []
        for meeting in intervals:
            sched.append((meeting.start, 1))
            sched.append((meeting.end, -1))
        
        sched.sort(key= lambda x: (x[0], x[1]))
        #print(sched)
        count = 0
        maxc = 0
        for key in sched:
            count += key[1]
            if count > maxc: maxc = count
            #print("at time", key[0], "maxc", maxc, "count=", count)

        return maxc

s = Solution()
intervals = addInterval([(0,40),(5,10),(15,20)])
print(s.minMeetingRooms(intervals)) #-->2
intervals = addInterval([(1,5),(2,6),(3,7),(4,8),(5,9)])
print(s.minMeetingRooms(intervals)) #--> 4
intervals = addInterval([(5, 10),(15,20),(0,30),(20,25),(10, 15)])
print(s.minMeetingRooms(intervals)) #-->2