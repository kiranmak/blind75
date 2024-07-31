'''
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''
from collections import deque
from typing import List, Optional
from treenode import TreeNode, makeTree


class Solution:
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        dq = deque([root])
        while len(dq) != 0:
            items = []
            length = len(dq)
            for i in range(length):
                node = dq.popleft()
                if node:
                    items.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            result.append(items)
        return result[:len(result)-1]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.traverse(root, 0, result)
        return result
        
    def traverse(self, root, level, ans):
        if root is None:
            return
        if len(ans) <= level:
            ans.append([])
        ans[level].append(root.val)
        self.traverse(root.left, level+1, ans)
        self.traverse(root.right, level+1, ans)
        return

s = Solution()
input = [3,9,20,None,None,15,7]
#input = [3]
root = makeTree(input)
root.print()
orderedList = s.levelOrder2(root)
print("orderedList=", orderedList)