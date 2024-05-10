class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next
    
class LinkedStack:
    def __init__(self):
        self.top=None
        self.size=0
        
    def isEmpty(self):
        return self.top==None

    def push(self,data):
        node=Node(data,self.top)
        self.top=node
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty.")
        else:
            p=self.top
            self.top=p.next
            self.size-=1
            return p.data
        
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.top.data
    
    def display(self):
        p=self.top
        for i in range(self.size):
            print("[%s]"%p.data,end=' ')
            p=p.next
        print()

if __name__=="__main__":
    S=LinkedStack()
    S.push('A');S.display()
    S.push('C');S.display()
    S.push('D');S.display()

    print('[%s] is popped'%S.pop());S.display()