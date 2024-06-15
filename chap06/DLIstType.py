# Double list node 전과 후를 가리키는 link field를 각 하나씩 가짐
class DListNode:
    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next

#Double linked deque
class DListType:
    def __init__(self):
        # front와 rear는 아무것도 안가리킨다.
        self.front=self.rear=None
        #최초 size는 0
        self.size=0
        
    #front에서 삽입
    def addFront(self,data):
        #일단 구슬을 손에 든다
        #addFront 즉, 내 앞에 아무도 없어야 하고, 내 뒤엔 현재의 맨 앞
        node=DListNode(data,None,self.front)
        #isEmpty 굳이 안쓰고 size로 판단
        if self.size==0:
            self.front=self.rear=node
        else:
            #self.front.prev는 None였다
            self.front.prev=node
            self.front=node
        self.size+=1
    
    def addRear(self,data):
        # 내 뒤에 아무도 없고 내 앞엔 현재의 맨 뒤
        node=DListNode(data,self.rear,None)
        # 비어있으면 rear와 front 모두 node를 가리킨다.
        if self.size==0:
            self.rear=self.front=node
        #비지 않았으면 기존 rear의 next가 node가 되고 rear는 node가 된다.
        else:
            #self.rear.next는 None였다.
            self.rear.next=node
            self.rear=node
        self.size+=1
        
    def addPos(self, pos, data):
        node=DListNode(data,None,None)
        if pos==1:
            self.addFront(data)
        elif pos==self.size+1:
            self.addRear(data)
        else:
            #현재 화살표는 1번에
            p=self.front
            #3번에 세워야지? 화살표는 3번에, 2번만 움직여야됨
            #2번에 세워야지? 화살표는 2번에, 1번만 움직임
            for i in range(1,pos):
                p=p.next
            #내가 무엇을 가리키는지?
            node.prev=p.prev
            node.next=p
            #무엇이 나를 가리키는지?
            p.prev.next=node
            p.prev=node
            
            self.size+=1
        
    def deleteFront(self):
        if self.size!=0:
            #return할 데이터 저장
            data=self.front.data
            #화살표 생성, 위치 1
            p=self.front
            # p.next는 2 이게 front가 됨.
            self.front=p.next
            #node가 한개라면 self.front가 None이 되어 버림
            if self.front==None:
                #self.rear가 유령 노드를 가리키기 때문에 None으로 초기화
                self.rear=None
            else:
                #self.front의 prev가 None이 됨.
                p.prev=None
            # node 삭제됐으므로 size -1
            self.size-=1
            return data
            
    def deleteRear(self):
        if self.size!=0:
            data=self.front.data
            #화살표 생성, 위치 마지막
            q=self.rear
            if self.rear==None:
                self.size-=1
    
    #과제는 아니지만 각자 만들어 보세요
    def deletePos(self,pos):
        if self.size!=0:
            if pos==self.size:
                self.deleteRear()
            elif pos==1:
                self.deleteFront()
            else:
                p=self.front
                for i in range(1,pos+1):
                    p=p.next
                p.next=
    def display(self):
        p=self.front
        while p!=None:
            print('[%c] <-> '%p.data, end='')
            p=p.next
        print('\b\b\b\b    ')
    
if __name__=="__main__":
    DL=DListType()
    # rear, front에 add하고 display
    DL.addRear('A');DL.addFront('B');DL.display()
    DL.addFront('C');DL.addRear('D');DL.display()
    DL.addPos(3,'E');DL.display()
    print('[%c] is deleted : '%DL.deleteFront(),end=' '); DL.display()