from CircularQueue import CircularQueue

class CircularDequeue(CircularQueue): #circular queue의 상속
    def __init__(self, capacity=10):
        super().__init__(capacity)
        
    def addRear(self,e):
        self.enqueue(e)
        
    def deleteFront(self):
        self.dequeue()
        
    def getFront(self):
        self.peek()
        
    def addFront(self,e):
        if not self.isFull():
            self.queue[self.front]=e
            self.front=(self.front-1+self.capacity)%self.capacity
        else:
            return print("Overflow")
        
    def deleteRear(self):
        if not self.isEmpty():
            e=self.queue[self.rear]
            self.rear=(self.rear-1+self.capacity)%self.capacity
            return e
        else:
            return print("Underflow")
    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        else:
            return print("Empty!")
        
if __name__=="__main__":
    import random
    DQ=CircularDequeue()
    for i in range(4):
        DQ.addFront(random.randint(65,90))
    DQ.display()
    
    for i in range(4):
        DQ.addRear(random.randint(65,90))
    DQ.display()
    
    for i in range(2):
        DQ.deleteFront()
    DQ.display()
    
    for i in range(2):
        DQ.deleteRear()
    DQ.display()