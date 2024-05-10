from CircularQueue import CircularQueue

map=[ 
    ['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1'],
]
SIZE=6 #미로의 크기

def isValidPos(row,col): #이 위치가 갈 수 있는 곳인가?
    if 0<=row<SIZE and 0<=col<SIZE:
        if map[row][col]=='0' or map[row][col]=='x':
            return True
        
    return False

def BFS():
    print('BFS :')
    Q=CircularQueue(50)
    Q.enqueue((1,0))
    while not Q.isEmpty():
        pos=Q.dequeue()
        (row, col)=pos #type:ignore
        if map[row][col]=='x': return True
        else:
            map[row][col]='.'
            if isValidPos(row-1,col): Q.enqueue((row-1,col))
            if isValidPos(row+1,col): Q.enqueue((row+1,col))
            if isValidPos(row,col-1): Q.enqueue((row,col-1))
            if isValidPos(row,col+1): Q.enqueue((row,col+1))
        Q.display2()
    return False #반복문이 끝났다는 것은 실패를 의미

if __name__=="__main__":
    result=BFS()
    if result:
        print("Success")
    else:
        print("Fail")