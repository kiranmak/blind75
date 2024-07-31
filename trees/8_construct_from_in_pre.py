'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''
from typing import List, Optional
from treenode import TreeNode, makeArray, makeTree

#strategy:
### left in[0:1], right [2:2]
# 

#solve for subtree(9,none) and subtree([20,15,7],[15,20,7]
#   solve subree([],[] ) and ([][])

class Solution:
    pindex = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 0 or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        inidx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:inidx+1], inorder[:inidx])
        root.right = self.buildTree(preorder[inidx+1:], inorder[inidx+1:])
        return root
       

#preorder, inorder = [3,9,20,15,7], [9,3,15,20,7]
preorder, inorder = [40,30,25,15,28,35,50,45,60,55,70], [15, 25,28,30, 35, 40,45,50, 55, 60,70]
s = Solution()
root = s.buildTree(preorder, inorder)
root.print()
arr = makeArray(root)
print("array of tree", arr)
newroot = makeTree(arr)
print("tree from array")
newroot.print()