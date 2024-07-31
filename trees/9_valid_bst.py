'''
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.  The right subtree of a node contains only nodes with keys greater than the node's key.  Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true
Example 2:
Input: root = [5,1,4,None,None,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
from typing import Optional
from treenode import TreeNode, makeTree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.left and root.left.val >= root.val:
           return False
        if root.right and root.right.val <= root.val:
           return False
        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)
        return (left and right)


#q = [2,1,3]
#q = [5,1,4,None,None,3,6]
#q = [3]
q = [5,4,6,None,None,3,7]
s = Solution()
root = makeTree(q)
print("first tree")
root.print()
ans = s.isValidBST(root)
print("tree isValid BST: ", ans)