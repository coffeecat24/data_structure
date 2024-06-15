Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

def rDFS(visited, u):
    visited[u] = True
    print(Vertex[u], end = ' ')
    for v in AdjVer[u]:
        if visited[v] == False:
            rDFS(visited, v)

if __name__ == "__main__":
    # 각 인덱스가 false라면 미방문, true면 이미 방문. 다시 못 감을 의미함
    visited = [False] * len(Vertex)
    print('rDFS(A) :', end = ' ')
    rDFS(visited, 0)