N = 100

class MaxHeap:
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0
        
    def upHeap(self):
        # 9 (1) 7 (2) 4 (5) 8 (11)
        i = self.heapSize   # i <- 11
        item = self.heap[i] # item <- 8
        
        while(i != 1) and (item > self.heap[i // 2]):
            self.heap[i] = self.heap[i // 2]  # H[11] <- 4, H[5] <- 7
            i = i // 2 # i <- 5, 2
        
        self.heap[i] = item # H[2] <- 8
    
    def insertItem(self, item):
        self.heapSize += 1
        self.heap[self.heapSize] = item
        # 완전 이진 트리 기반으로 확장되어 간다는 것을 지켜줌
        
        self.upHeap()
        
    def downHeap(self):
        item = self.heap[1] # item <- 3
        parent = 1
        child = 2
        
        while child <= self.heapSize: # 2 <= 10 ?
            if (child < self.heapSize) and (self.heap[child + 1] > self.heap[child]):
            # 왼쪽 자식만 있냐 오른쪽 자식도 있냐 오른쪽 자식도 있어야 둘 비교..
                child += 1
            
            if item >= self.heap[child]:
                break
            
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2
        
        self.heap[parent] = item
    
    def removeItem(self):
        item = self.heap[1] # item <- 9
        self.heap[1] = self.heap[self.heapSize] # root <- 3
        self.heapSize -= 1
        self.downHeap()
        
        return item
    
if __name__ == "__main__":
    H = MaxHeap()
    data = [7, 3, 5, 6, 4, 9, 2, 3, 1, 2]
    
    for e in data:
        H.insertItem(e)
        print('Heap :', H.heap[1:H.heapSize + 1])
    print()
    
    print('[%d] is deleted' %H.removeItem())
    print('Heap :', H.heap[1:H.heapSize + 1])
    print('[%d] is deleted' %H.removeItem())
    print('Heap :', H.heap[1:H.heapSize + 1])    