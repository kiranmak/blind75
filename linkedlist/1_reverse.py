'''
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''
from typing import Optional
from listnode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        c = head
        n = head.next
        head.next = None
        while n:
            cn = n.next
            n.next = c
            c = n
            n = cn
        head = c
        return head

if __name__ == '__main__':
    s = Solution()
    dummy = ListNode(-1, None)
    lhead = dummy.makeList([1,2,3,4,5])
    #lhead = s.makeList([1,2])
    if lhead:
        lhead.print()
    rhead = s.reverseList(lhead)
    if rhead:
        rhead.print()
