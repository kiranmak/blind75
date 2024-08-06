# Definition for singly-linked list.
from heapq import heappop, heappush
from typing import Optional
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def show(self):
        curr = self
        print("Head", end=": ")
        while curr: 
            print(curr.val, "->", end="")
            curr = curr.next

        print("None")
        
class List:
    def __init__(self):
        self.head = None

    def makeList(self, arr):
        self.head = ListNode(arr[0])
        curr = self.head
        for val in arr[1:]:
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        return self.head
            

def le(self, other):
    return self.val < other.val
def eq(self, other):
    return self.val == other.val
ListNode.__eq__ = eq
ListNode.__le__ = le
    
#ListNode.__eq__: lambda self, other: self.val == other.val
#ListNode.__le__: lambda self, other: self.val < other.val
class Solution:
    def mergeKLists(self, lists)-> Optional[ListNode]:
        '''
         algorithm
         1. start with smallest of each list and heapify.
         2. pick smallest, add to result list. 
         3. move its next to back of heap and heapify
         4. go on till heap is empty.
        '''
        pq = []
        for li in lists:
            if li:
                heappush(pq, (li.val, li))
        
        dummy = ListNode(-sys.maxsize)
        result = dummy
        
        while pq:
            val, node = heappop(pq)
            result.next = node
            result = result.next
            if node.next:
                heappush(pq, (node.next.val, node.next))
        
        result = dummy.next
        return result
    
arrs = [[1,4,5],[1,3,4],[2,6]]
l1, l2, l3 = List(), List(), List()
h1 = l1.makeList(arrs[0])
h2 = l2.makeList(arrs[1])
h3 = l3.makeList(arrs[2])
s = Solution()
result = s.mergeKLists([h1,h2,h3])    
result.show() 
h1.show() 