import sys

INSERT = 'I'
DELETE = 'D'
MAXIMUM = 'M'
MAX_CAPACITY = 1000
INT_MIN = -sys.maxsize

class MaxHeap:
    def __init__(self, num=MAX_CAPACITY):
        self.elements = [0] * num
        self.count = 0
        self.capacity = num

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def insertElement(self, elem):
        if self.count >= self.capacity:
            raise Exception("Heap Overflow!")
        i = self.count
        self.count += 1
        self.elements[i] = elem
        while i > 0 and self.elements[self.parent(i)] < self.elements[i]:
            temp = self.elements[i]
            self.elements[i] = self.elements[self.parent(i)]
            self.elements[self.parent(i)] = temp
            i = self.parent(i)
        return elem

    def maximum(self):
        return self.elements[0]

    def deleteMaximum(self):
        if self.count < 1:
            raise Exception("Heap Underflow!")
        root = self.elements[0]
        self.elements[0] = self.elements[self.count-1]
        self.count -= 1
        if self.count > 0:
            self.maxHeapify(0)
        return root

    def maxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.count and self.elements[l] > self.elements[i]:
            largest = l
        if r < self.count and self.elements[r] > self.elements[largest]:
            largest = r
        if largest != i:
            temp = self.elements[i]
            self.elements[i] = self.elements[largest]
            self.elements[largest] = temp
            self.maxHeapify(largest)

def heap_sort(arr):
    max_heap = MaxHeap(len(arr))
    
    for elem in arr:
        max_heap.insertElement(elem)
    
    sorted_arr = []
    while max_heap.count > 0:
        sorted_arr.append(max_heap.deleteMaximum())
    
    return sorted_arr[::-1]  # Reverse to get ascending order

N = int(sys.stdin.readline())
li = []

for i in range(N):
  li.append(int(input()))

li = heap_sort(li)

for x in li:
  print(x)