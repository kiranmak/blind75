
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toArray(self):
        arr = []
        arr.append(self.val)
        node = self.next
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def print(self):
        print("H:", self.val, end="")
        node = self.next
        while node:
            print("->", node.val, end="")
            node = node.next
        print(".")
    
    def makeList(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0], None)
        curr = head

        for item in arr[1:]:
            newnode = ListNode(item, None) 
            curr.next = newnode
            curr = newnode
        return head
    
    def makeCycleList(self, arr, pos):
        head = ListNode(arr[0], None)
        curr = head
        cycle = None
        for item in arr[1:]:
            newnode = ListNode(item, None) 
            curr.next = newnode
            curr = newnode
            if arr[pos] == item:
                cycle = curr
        if pos == 0:
            cycle = head
        curr.next = cycle
        return head

    def printCycle(self, count):
        print("H:", self.val, end="")
        node = self.next
        n = 0
        while node and count > n:
            print("->", node.val, end="")
            node = node.next
            n += 1
        print(".")
