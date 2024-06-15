from ListNode import ListNode
from ListType import ListType

S=ListType()
def push(data):
    S.insertFirst(data)
    
def pop():
    return S.deleteFirst()

push('A');S.display()
push('C');S.display()
push('D');S.display()

print('[%s] is popped'%pop());S.display()