from ListNode import ListNode

#List를 위해서 새로 구현한 데이터 타입.
#리스트 노드는 구슬, 리스트 타입은 목걸이
class ListType:
    def __init__(self):
        self.head = None
        self.size = 0 #optional, None을 만날 때 까지 함수를 이용해서 구할 수도 있음
    
    def isEmpty(self):
        return self.head==None #self.size를 추가한 경우 self.size==0으로도 가능
    
    #insertfirst랑 insertposition이 둘 다 있는게 좋다. 필요하다면 insertlast도.
    def insertFirst(self, data):
        #insert에서 제일 처음 할 것은? 노드를 만든다. 구슬을 만든다.
        node = ListNode(data, self.head)
        self.head=node #내가 첫번째 노드가 된다.
        self.size+=1
    
    def getNode(self,pos):
        p=self.head
        for i in range(1,pos-1):
            p=p.next
        
        return p #pos 이전 노드의 주소(위치)
    
    def insert(self,pos,data):
        if pos==1:
            self.insertFirst(data)
        else:
            if pos<=self.size+1:
                p=self.getNode(pos)
                node=ListNode(data,p.next)
                p.next=node
                self.size+=1
            else:
                print("Invalid Position")
                
    def deleteFirst(self):
        if self.isEmpty():
            print("No element")
        else:
            p=self.head #화살표를 만든다. 첫번째 노드를 가리킴.
            self.head=p.next #self.head에 첫번째 노드의 다음 노드의 주소를 입력
            self.size-=1 #노드 없어지니 size 1 줄임.
            return p.data
        
    def delete(self,pos):
        if self.isEmpty():
            print("No element")
            return
        if pos==1:
            return self.deleteFirst()
        else:
            if pos<=self.size: #insert에서는 size 이후 하나가 더 들어와도 insert 수행이지만, delete는 size 이후에 원소 x
                p=self.getNode(pos)
                q=self.getNode(pos+1)
                p.next=q.next
                self.size-=1
                return q.data
            else:
                print("Invalid Position")
    
    def display(self):
        p=self.head #화살표, self.head
        #화살표가 가리키는 값이 Node야? yes 출력, 다음 주소로, None면? 종료
        while p!=None:
            print('[%s] ->'%p.data, end=' ')
            p=p.next
        print('\b\b\b   ')
        
        
if __name__=="__main__":
    L=ListType() #한 손에 선을 들었다
    L.insertFirst('A')
    L.insertFirst('B')
    L.display()
    
    L.insert(2,'C')
    L.insert(1,'D')
    L.insert(4,'E')
    L.insert(5,'F')
    L.display()
    print('[%s] is deleted.'%L.deleteFirst())
    L.display()
    print('[%s] is deleted.'%L.delete(1))
    L.display()
    print('[%s] is deleted.'%L.delete(4))
    L.display()
    print('[%s] is deleted.'%L.delete(2))
    L.display()