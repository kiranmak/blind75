"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional
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

dummy = ListNode(-1, None)
list1 = dummy.makeList([])            
list2 = dummy.makeList([])            
#list1 = dummy.makeList([1,2,4])            
#list2 = dummy.makeList([1,3,4])            
s = Solution()
ans = s.mergeTwoLists(list1, list2)
if ans: ans.print()
            