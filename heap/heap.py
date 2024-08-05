
class Heap:
    def __init__(self, minHeap):
       self.arr = []
       self.isMin = minHeap

    def swap(self, f, s):
        temp = self.arr[f]
        self.arr[f],self.arr[s] = self.arr[s], temp
        
    def left(self, index):
        return index*2 + 1

    def right(self, index):
        return index*2 + 2

    def parent(self, index):
        return (index-1)//2

    def left_val(self, index):
        return self.arr[index*2//2]

    def right_val(self, index):
        return self.arr[index*2//2 + 1]

    def parent_val(self, index):
        return self.arr[(index-1)//2]
        
    def remove(self): # always top
       n = len(self.arr)
       if n == 0:
           return
       self.arr[0] = self.arr[n-1]
       if len(self.arr) <= 1:
           return
       self.downheap(0)

    def insert(self, item):
       self.arr.append(item)
       if len(self.arr) > 1:
           self.upheap(len(self.arr)-1)

    def upheap(self, index):
       p = self.parent(index)
       if p < 0:
           return
       if self.arr[p] > self.arr[index]:
           self.swap(p,index)
           self.upheap(p)
    
    def downheap(self, index):
       r = self.right(index)
       l = self.left(index)
       i = index
       n = len(self.arr)
       if r < n and self.arr[r] < self.arr[i]:
           self.swap(r, i)
           i = r
       elif l < n and self.arr[l] < self.arr[i]:
           self.swap(l, i)
           i = l
       else:
           return
       self.downheap(i)
    
    def makeHeap(self, arr):
        self.arr = arr
        nonLeafIdx = len(arr)//2 
        for index in range(nonLeafIdx, -1, -1):
            #print("heapify: ", index)
            self.heapify(index)
    
    def heapify(self, index):
        n = len(self.arr)
        smallest = index
        l = self.left(index)
        r = self.right(index)
        if l < n and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < n and self.arr[r] < self.arr[smallest]:
            smallest = r
        self.swap(smallest, index)

    def show(self):
        print(self.arr)
       
    
minheap = Heap(minHeap=True)
'''
minheap.insert(3)
minheap.show()
minheap.insert(4)
minheap.show()
minheap.insert(9)
minheap.show()
minheap.insert(5)
minheap.show()
minheap.insert(2)
minheap.show()
'''
print("orig", [3,9,2,5,4,1])
minheap.makeHeap([3,9,2,5,4,1])
print("heap ", end="")
minheap.show()