'''
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
    4
 2    7
1 3  6 9  
    4
 7    2
9 6  3 1  

    4
 2    7
1      9  
    4
 7    2
9      1  

     4
  2    7
 1         
  0

     4
  7    2
         1    
       0


Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from treenode import TreeNode, makeTree, makeArray


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left = r
        root.right = l
        return root
        

s = Solution()
input= [4,2,None,1,3,None, None, 6,None, None, 9]
#input= [2,1,3]
#input = [4,2,7,1,3,6,9]
root = makeTree(input)
root.print()
root = s.invertTree(root)
print("invered tree=")
root.print()
arr = makeArray(root)
print(input)
print(arr)