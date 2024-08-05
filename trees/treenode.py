
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = None
        self.right = None
        self.val = val
        
    def addLeft(self, val):
        l = TreeNode(val)
        self.left = l
        return l

    def addRight(self, val):
        l = TreeNode(val)
        self.right = l
        return l

    def isLeaf(self):
        return False if self.left or self.right else True

    def print(self):
        root = self
        self.inorder(root, "ro", 0)

    def inorder(self, node, tag, level):
        if not node:
            return
        spaces = "".join(["    "] * level)
        print(spaces, tag, "->", node.val)
        
        self.inorder(node.left, "L", level + 1)
        self.inorder(node.right, "R", level + 1)

def makeTree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    i = 1
    node = root
    n = i
    dq = deque([root])
    while len(dq) != 0 and n < len(arr):
        node = dq.popleft()
        if not node.left:
            if arr[n] != None:
                left = node.addLeft(arr[n])
                dq.append(left)
            n += 1
        if n == len(arr):
            break

        if not node.right:
            if arr[n] != None:
                right = node.addRight(arr[n])
                dq.append(right)
            n += 1
    return root

def parent(root, val):
    if not root:
        return  None
    if root.val == val:
        return root
    
    left = root.left
    if left.val == val:
        return root
    if left.val > val: 
        return parent(root.left, val)
    return parent(root.right, val)

def makeArray(root):
    if not root:
        return None
    dq = deque([root])
    arr = []
    while 0 != len(dq):
        node = dq.popleft()
        if not node:
            arr.append(None)
            pass
        else:
            arr.append(node.val)
            dq.append(node.left)
            dq.append(node.right)
    while arr[-1] is None:
        del arr[-1]
    return arr

if __name__ == '__main__':
    '''
    root = TreeNode(4)
    
    n1 = root.addLeft(3)
    n2 = root.addRight(12)
    n11 = n1.addLeft(6)
    n12 = n1.addRight(7)
    n21 = n2.addLeft(65)
    n22 = n2.addRight(10)
    '''
    aa = [ [1,2], [1,2,3], [1,None,3], [1,2,3,4],
           [1,2,3,4,5], [3,9,20,None,None,15,7]]

    for arr in aa:
        root = makeTree(arr)
        print("Tree for", arr)
        root.print()
        print("----------")

    input, val = [3,9,20,None,None,15,7], 15
    root = makeTree(input)
    node = parent(root, val)
    if node:
        print("parent of ", val, "is", node.val)
    else:
        print("None")