"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""
from typing import List, Optional
from lc_1_reverse import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None:
            return None

        slow, fast, i = head, head, 0

        while fast and i < n:
            fast = fast.next
            i+=1
        prev_nth = None
        while fast:
            print("fast=", fast.val, "slow=", slow.val)
            prev_nth = slow
            slow = slow.next
            fast = fast.next
        
        # if head
        if slow == head:
            head = head.next
        else:    
            prev_nth.next = slow.next
        return head
    
dummy = ListNode(-1, None)
list2 = dummy.makeList([1,2,3,4,5])
list1 = dummy.makeList([1,2])
s = Solution()
ans = s.removeNthFromEnd(list1, 2)
if ans: ans.print()
print("----")
ans = s.removeNthFromEnd(list1, 1)
if ans: ans.print()
print("----")
ans = s.removeNthFromEnd(list2, 2)
if ans: ans.print()
        