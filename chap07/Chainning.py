class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

M = 13

# 헤드 포인터를 배열로 만들 것이다.

class HashTable:
    def __init__(self):
        self.table = [None] * M
    
    def hashFn(self, key):
        return key % M
    
    def insert(self, key):
        b = self.hashFn(key)
        node = Node(key)
        node.next = self.table[b] #insertFirst.. 테이블이 바로 가리키게끔
        self.table[b] = node
        
    # None을 만날 때까지 자기가 원하는 값이 있는지 탐색..
    # 연결리스트로 삭제..
    
    def display(self):
        for i in range(M):
            print('HT[%02d] : ' % i, end = '')
            n = self.table[i]
            if n == None:
                print()
            else:
                while n is not None:
                    print(n.data, end = ' ')
                    n = n.next
                print()
                
if __name__ == '__main__':
    import random
    
    HT = HashTable()
    
    for i in range(20):
        HT.insert(random.randint(10,99))
    
    HT.display()