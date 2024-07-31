'''
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
   -10
   9  20
$  $  15 7
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
from typing import Optional
from treenode import TreeNode, makeArray, makeTree


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [-sys.maxsize]
        val = self.dfs(root, result)
        return result[0]

    def dfs(self, root, ans):
        if root is None:
            return 0

        # get sum from left tree
        leftsum  = self.dfs(root.left, ans)
        rightsum = self.dfs(root.right, ans)
        leftsum = 0 if leftsum < 0 else leftsum
        rightsum = 0 if rightsum < 0 else rightsum

        ans[0] = max(ans[0], root.val + leftsum + rightsum)

        return max(rightsum, leftsum) + root.val

s = Solution()
input = [-10,9,20,None,None,15,7]
#input = [1,2,3,None,None,5,4]
#input= [2,1,3]
root = makeTree(input)
root.print()
sum = s.maxPathSum(root)
print("maxPathSum =", sum)
#arr = makeArray(root)
#print(input)
#print(arr)

