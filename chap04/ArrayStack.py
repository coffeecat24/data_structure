class ArrayStack:
    def __init__(self,capacity=100):
        self.capacity= capacity
        self.stack=[None]*self.capacity
        self.top=-1
        
    def isEmpty(self):
        return self.top==-1
    
    def isFull(self):
        return self.top==self.capacity-1
    
    def push(self,e):
        if not self.isFull():
            self.top+=1
            self.stack[self.top]=e
        else:
            print('Overflow')
            
    def pop(self):
        if not self.isEmpty():
            e=self.stack[self.top]
            self.top-=1
            return e
        else:
            print('Empty!')
            
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        
    def display(self):
        print(self.stack[self.top::-1])
        
    def sortedPush(self,e):
        if(self.isEmpty() or e>self.peek()):
            self.push(e)
        else:
            tmp=self.pop()
            self.sortedPush(e)
            self.push(tmp)
        
if __name__=="__main__":
    S=ArrayStack(10)
    data=[5,3,8,1,2,7]
    for d in data:
        S.sortedPush(d)
        S.display()
        
    print(S.pop())
    S.display()
    
    print(S.peek())
    S.display()