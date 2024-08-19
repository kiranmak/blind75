"""
Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

Given a binary tree and a particular node, find all cousins of that node.
"""

from collections import deque
from treenode import makeTree

# intuition
# traverse bfs  - all nodes at same level will be in queue.
# now somehow check if there parent is same or not.
# dfs way:
# traverse tree and measure from the bottom as you go up.
# check for hts is same
def areCousins(root, val):
    if root is None:
        return []
    res = []
    def dfs(node, val, level):
            
        if node is None:
            return -1, None
        if node.left and node.left.val == val:
            return level + 1, node
        if node.right and node.right.val == val:
            return level + 1, node

        x, parent = dfs(node.left, val, level + 1)
        if x == -1:
            x, parent = dfs(node.right, val, level + 1)
        return x, parent
    
    def cousins(node, mylevel):
        if node is None:
            return
        # my children are at same level.
        if (mylevel + 1) == level and parent.val != node.val:
            if node.left: res.append(node.left.val)
            if node.right: res.append(node.right.val)
            return

        if (mylevel + 1) > level:
            return 

        cousins(node.left, mylevel+1)
        cousins(node.right, mylevel+1)
                
    level, parent = dfs(root, val, 0)
    print("level", level, "parent", parent.val)
    #cousins
    cousins(root, 0 )
    return res
        
    
p =  [1,2,3, 4, 5, 6, 7, None, None, None, None, 8,9]
pp = makeTree(p)
pp.print()
ans = areCousins(pp, 6)
print("tree level: ", ans)