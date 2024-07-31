'''
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''
from collections import deque
from typing import Optional
from treenode import TreeNode, makeTree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        pr, qr = p, q
        dq = deque([(p,q)])
        while len(dq) > 0:
            first, second = dq.popleft()
            if first and second:
                if first.val != second.val:
                    return False
                dq.append((first.left, second.left))
                dq.append((first.right, second.right))
        return True
            

s = Solution()
#p, q = [1,2,3], [1,2,3]
p, q = [1,2], [1,None,2]
pp = makeTree(p)
qq = makeTree(q)
print("first tree")
pp.print()
print("second tree")
qq.print()
ans = s.isSameTree(pp,qq)
print("tree same: ", ans)