"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
from treenode import TreeNode, makeTree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = self.inorderTraversal(root, 0)
        return ans
        
    def inorderTraversal(self, root, level):
        if not root:
            return 0
        l = 1 + self.inorderTraversal(root.left, level + 1)
        r = 1 + self.inorderTraversal(root.right, level + 1)
        return max(l,r)

s = Solution()
root = makeTree([3,9,20,None,None,15,7])
root.print()
depth = s.maxDepth(root)
print("maxDepth=", depth)
root = makeTree([])
root = makeTree([3,9,None, None,15,7])
root.print()
depth = s.maxDepth(root)
print("maxDepth=", depth)
