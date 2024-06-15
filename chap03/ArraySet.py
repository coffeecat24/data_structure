class ArraySet:
    def __init__(self,capacity=100):
        self.capacity=capacity
        self.array=[None]*self.capacity
        self.size=0
        
    def __eq__(self,setB):
        if self.size!=setB.size:
            return False
        for i in range(setB.size):
            if not self.contains(setB.array[i]):
                return False
        return True
            
    
    def isEmpty(self):
        return self.size==0
    
    def isFull(self):
        return self.size==self.capacity
    
    def display(self):
        for i in range(self.size):
            print(self.array[i],end=' ')
        print()
        
    def contains(self, e):
        for i in range(self.size):
            if self.array[i]==e:
                return True
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size]=e
            self.size+=1
            
    def delete(self,e):
        for i in range(self.size):
            if self.array[i]==e:
                self.array[i]=self.array[self.size-1]
                self.size-=1
    
    def union(self, setB):
        setC=ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
        
        for i in range(setB.size):
            setC.insert(setB.array[i])
        
        return setC
    
    def intersection(self,setB):
        setC=ArraySet()
            
        for i in range(setB.size):
            for j in range(self.size):
                if self.array[j]==setB.array[i]:
                    setC.insert(self.array[j])
        
        return setC
                
    
    def difference(self,setB):
        setC=ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
            
        for i in range(setB.size):
            setC.delete(setB.array[i])
            
        return setC
            
if __name__=='__main__':
    S=ArraySet()
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(40)
    S.display()
    
    T=ArraySet()
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(10)
    T.display()
    
    S.union(T).display()
    
    S.intersection(T).display()
    
    S.difference(T).display()
    S1=ArraySet()
    S1.insert(10)
    S1.insert(20)
    S1.insert(30)
    S1.insert(40)
    S1.display()
    print(S==T)
    print(S==S1)
    
    #교집합, 차집합 연산
    #print(S==T): 연산자 중복