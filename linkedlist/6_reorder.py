"""
143. Reorder List
Medium
Topics
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
h  n     p  t
1->2->3->4->5->6->7->8

s  s  s  s  
f     f    f        f
           8-7-6-5
1-8-2-7-3-6-4-5           
from head to slow
reverse slow to end
1-2-5-4-3
- h->next - slow


h:1->3
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""
from typing import Optional
from listnode import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second, prev = slow.next, slow
        prev.next = None
        while second:
            save = second.next
            second.next = prev
            prev = second
            second = save 

        first,second = head, prev
        while first and second: 
            tmp_f, tmp_s = first.next, second.next
            first.next = second
            second.next = tmp_f
            first, second = tmp_f, tmp_s
            
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow, fast = head, head.next
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        
        return True if slow == fast else False

dummy = ListNode(-1, None)
list1 = dummy.makeList([1,2,3,4,5 ])
s = Solution()
s.reorderList(list1)
if not s.hasCycle(list1):
    list1.print()
else:
    print("has cycle")
    list1.printCycle(6)