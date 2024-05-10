#back tracking 스택을 이용해서
#3번에서 갈 수 있는 곳 없으면 3 pop한다.
#4에서 3 제외 또 갈 수 있는 곳 찾아간다 5
#5 pop, 6으로, 7로
#깊이 우선 탐색 노드를 전부 다 순회하는 알고리즘
from ArrayStack import ArrayStack

map=[ 
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1'],
]
SIZE=6 #미로의 크기

def isValidPos(row,col): #이 위치가 갈 수 있는 곳인가?
    if 0<=row<SIZE and 0<=col<SIZE:
        if map[row][col]=='0' or map[row][col]=='x':
            return True
        
    return False

def DFS():
    print('DFS : ')
    S=ArrayStack(100)
    S.push((1,0)) #최초 좌표 1행 0열을 S에 push
    while not S.isEmpty():#초기값을 넣은 후에 반복문에 들어감 적절하게 반복하면 됨 일반적임
        pos=S.pop()
        print(pos,end=' -> ')
        (row, col)=pos #type:ignore
        if(map[row][col]=='x'):
            return True
        else:
            map[row][col]='.'
            if isValidPos(row-1,col): S.push((row-1,col))
            if isValidPos(row+1,col): S.push((row+1,col))
            if isValidPos(row,col-1): S.push((row,col-1))
            if isValidPos(row,col+1): S.push((row,col+1))
        S.display()
    
    return False

if __name__=="__main__":
    result=DFS()
    if result:
        print("Success")
    else:
        print("Fail")