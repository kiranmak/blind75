"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

from typing import List, Optional
from lc_1_reverse import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None: return list2
        if list2 is None: return list1
        
        l1, l2 = list1, list2
        newlist = None
        
        if l1 and l2:
            if l1.val <= l2.val:
                newlist = l1
                l1 = l1.next
            else:
                newlist = l2
                l2 = l2.next
        newHead = newlist

        while l1 and l2:
            if l1.val <= l2.val:
                newlist.next = l1
                l1 = l1.next
            else:
                newlist.next = l2
                l2 = l2.next
            newlist = newlist.next
        if not l1:
            newlist.next = l2
        if not l2:
            newlist.next = l1
        return newHead

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return []
        
        ans = self.mergeHelper(lists, 0, len(lists)-1)
        return [] if  ans is None else ans
        
    def mergeHelper(self, lists, st, end): 
        if st == end:
            return lists[st]
        
        if end - st == 1:
            return self.mergeTwoLists(lists[st], lists[end])
            
        mid = st + (end - st)//2
        left = self.mergeHelper(lists, st, mid)
        right = self.mergeHelper(lists, mid+1, end)
        return self.mergeTwoLists(left, right)

dummy = ListNode(-1, None)
list1 = dummy.makeList([1,4,5])            
list2 = dummy.makeList([1,3,4])            
list3 = dummy.makeList([2,6])            

s = Solution()
ans = s.mergeKLists([[]])
#ans = s.mergeKLists([list1, list2, list3])
#if ans: ans.print()
print(ans)
