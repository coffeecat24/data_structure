class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next
    
class CircularQueue:
    def __init__(self):
        self.tail=None
        self.size=0
        
    def isEmpty(self):
        return self.tail==None
    
    def enqueue(self, data):
        node=Node(data,None)
        if self.isEmpty():
            node.next=node
            self.tail=node
        else:
            node.next=self.tail.next
            self.tail.next=node
            self.tail=node
        self.size+=1
        
    def display(self):
        if self.isEmpty():
            print("No Elements")
            return
        p=self.tail.next
        
        for i in range(self.size):
            print('[%s] ->'%p.data, end=' ')
            p=p.next
        
        print('\b\b\b   ')
        
    def dequeue(self):
        if not self.isEmpty():
            p=self.tail
            q=p.next
            data=q.data
            if p==q:
                self.tail=None
            else:
                p.next=q.next
            self.size-=1
            return data
        else:
            print("No Elements")
if __name__=='__main__':
    Q=CircularQueue()
    
    Q.enqueue('A');Q.display()
    Q.enqueue('C');Q.display()
    Q.enqueue('B');Q.display()
    print('[%s] is deleted'%Q.dequeue());Q.display()
    print('[%s] is deleted'%Q.dequeue());Q.display()
    print('[%s] is deleted'%Q.dequeue());Q.display()
    
    #오늘의 과제
    #링크드 스택 구현 지금 방금 전에 구현한 방식으로 직접 push pop peek 다 함수 만들고 node 다 지금 만든 것처럼 해서
    #queue는 단순 연결 구조의 큐 원형 연결 구조가 아니라. front rear 두 개의 포인터를 이용해서 선형 큐 만들기
    #이번주 일요일 자정까지