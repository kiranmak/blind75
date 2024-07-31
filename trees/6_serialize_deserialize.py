'''
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from treenode import TreeNode, makeTree


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []

        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node:
                dq.append(node.left)
                dq.append(node.right)
                res.append(str(node.val))
            else:
                res.append("None")
                
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        tokens = data.split(',')
        root = TreeNode(int(tokens[0]))
        dq = deque([root])
        i = 1
        while dq and i <= len(tokens):
            parent = dq.popleft()
            l,r = None, None
            if tokens[i] != "None":
                l = TreeNode(int(tokens[i]))
                parent.left = l
                dq.append(l)
            i += 1

            if tokens[i] != "None":
                r = TreeNode(int(tokens[i]))
                parent.right = r
                dq.append(r)
            i += 1
        return root
                 

# Your Codec object will be instantiated and called as such:
input = [1,2,3,None,None,4,5]
root = makeTree(input)
root.print()
ser = Codec()
deser = Codec()
#ans = deser.deserialize(ser.serialize(root))
print("serialize")
ans = ser.serialize(root)
print(ans)
tr_ans = deser.deserialize(ans)
print("deserialize")
tr_ans.print()
