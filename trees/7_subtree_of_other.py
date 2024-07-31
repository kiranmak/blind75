
'''
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''
from typing import Optional

from treenode import TreeNode, makeTree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.match(root, subRoot):
            return True
        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r

    def match(self, root, subRoot):
        if not subRoot and not root:
            return True
        if root and subRoot and root.val == subRoot.val:
            l = self.match(root.left, subRoot.left)
            r = self.match(root.right, subRoot.right)
            return (l and r)


    def isSubtree2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
                return True
        if root is None:
            return False

        if not root and not subRoot:
            return True

        if subRoot and root and subRoot and root.val == subRoot.val:
            l = self.isSubtree(root.left, subRoot.left)
            r = self.isSubtree(root.right, subRoot.right)

            return (l and r)

        ans = self.isSubtree(root.left, subRoot)
        if not ans:
            ans = self.isSubtree(root.right, subRoot)
        return ans       

        
#arr, subArr = [3,4,5,1,2], [4,1,2]
arr, subArr = [2,2], [2]
#arr, subArr = [3,4,5,1,2,None,None,None,None,0], [4,1,2]
s = Solution()
root = makeTree(arr)
subRoot = makeTree(subArr)

print("Tree for", arr)
root.print()
print("Tree for", subArr)
subRoot.print()
ans = s.isSubtree2(root, subRoot)
print("ans=", ans)