'''
295. Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the 
list is even, there is no middle value, and the median is the mean of the 
two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 
of the actual answer will be accepted.
Example 1:
Input ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would
you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], 
how would you optimize your solution?
'''
from heapq import *
import sys

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            val = heappushpop(self.small, -num)
            heappush(self.large, -val)
        else:
            val = heappushpop(self.large, num)
            heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

        
input = [[],[12],[],[10],[],[13],[],[11],[],[5],[],[15],[],[1],[],[11],[],[6],[],[17],[],[14],[],[8],[],[17],[],[6],[],[4],[],[16],[],[8],[],[10],[],[2],[],[12],[],[0],[]]
actions = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]

print("input", input[0])
mf = MedianFinder()
for i in range(len(actions[1:])):
    if actions[i] == "addNum":
        mf.addNum(input[i][0])
    elif actions[i] == "findMedian":
        print("left=", mf.small, "right=", mf.large)
        ans = mf.findMedian()
        print("findMedian", ans)
    continue
    
'''
Output
[null,null,12.00000,null,11.00000,null,12.00000,null,11.00000,null,11.00000,null,11.50000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,11.00000,null,10.50000,null,10.00000,null,10.50000,null,10.00000]
Expected
[null,null,12.00000,
      null,11.00000,
      null,12.00000,
      null,11.50000,
      
      null,11.00000,
      null,11.50000,
      null,11.00000,
      null,11.00000,
      
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,11.00000,
      null,10.50000,
      null,10.00000,
      null,10.50000,
      null,10.00000]

mf = MedianFinder()
medianFinder.addNum(1) # arr[1]
medianFinder.addNum(2)       #arr = [1, 2]
ans = medianFinder.findMedian()    #return 1.5 (i.e., (1 + 2) / 2)
print("ans", ans)
medianFinder.addNum(3)       #arr[1, 2, 3]
ans = medianFinder.findMedian()    #return 2.0
print("ans", ans)
'''