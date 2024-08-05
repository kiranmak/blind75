'''
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
'''
from treenode import TreeNode, makeTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans= self.inorder(root, p, q)
        return ans
        
    def inorder(self, root, p, q):
        if not root:
            return None

        # this condition will stop when == and node is found
        if root.val > p and root.val > q:
            return self.inorder(root.left, p,q)
        if root.val < p and root.val < q:
            return self.inorder(root.right, p,q)
        return root
            
        
s = Solution()
#input= [4,2,None,1,3,None, None, 6,None, None, 9]
input, p, q = [6,2,8,0,4,7,9,None,None,3,5], 2, 7
#input, p, q = [2,1], 2, 1

root = makeTree(input)
root.print()
ans = s.lowestCommonAncestor(root, p,q)
if ans:
    print("LCA in tree for", p, "and", q , "is", ans.val)
else:
    print("root is none")
