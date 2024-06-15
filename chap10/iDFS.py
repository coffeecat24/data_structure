Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

from queue import LifoQueue
visited = [False] * len(Vertex)

def iDFS(u):
    S = LifoQueue()
    S.put(u)
    
    while not S.empty():
        u = S.get()
        S.put(u) # peek
        
        if visited[u] == False:
            visited[u] = True
            print(Vertex[u], end = ' ')
        
        flag = True
        
        for v in AdjVer[u]:
            # 인접 정점 중 방문 안한 곳이 없으면 탐색 실패
            if visited[v] == False:
                S.put(v)
                # 인접 정점으로 이동했으므로, falg를 변경
                flag = False
                break
        
        if flag == True:
            S.get()

if __name__ == "__main__":
    print('iDFS(A) :', end = ' ')
    iDFS(0)