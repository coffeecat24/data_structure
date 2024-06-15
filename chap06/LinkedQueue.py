class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

class LinearQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    
    def isEmpty(self):
        return self.front==None
    
    def enqueue(self,data):
        node=Node(data,None)
        if self.isEmpty():
            self.front=node
            self.rear=node
            self.size+=1
        else:
            p=self.rear
            p.next=node
            self.rear=node
            self.size+=1
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            p=self.front
            self.front=p.next
            self.size-=1
            return p.data
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        else:
            p=self.front
            for i in range(self.size):
                print("[%s]"%p.data,end=' ')
                p=p.next
            print()

if __name__=="__main__":
    Q=LinearQueue()
    
    Q.enqueue('A');Q.display()
    Q.enqueue('C');Q.display()
    Q.enqueue('B');Q.display()
    print('[%s] is deleted'%Q.dequeue());Q.display()
    print('[%s] is deleted'%Q.dequeue());Q.display()
    print('[%s] is deleted'%Q.dequeue());Q.display()