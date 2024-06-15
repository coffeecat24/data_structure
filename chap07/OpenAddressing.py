M = 13
table = [0] * M

def hashFn(key):
    return key % M

def hashFn2(key):
    # 여기서도 prime number 쓰는데, M보다 작은 최대 소수
    return 11 - (key % 11)

def getLinear(v, i):
    return (v + i) % M

def getQuadratic(v, i):
    return (v + i * i) % M

def getDouble(v, i, key):
    return (v + i * hashFn2(key)) % M

def insert(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        #b = getQuadratic(v, i)
        #b = getDouble(v, i, key)
        
        if table[b] == 0:
            table[b] = key
            return
        
        else:
            i += 1

def search(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        #b = getQuadratic(v, i)
        #b = getDouble(v, i, key)
        
        print('[%d] '%table[b], end = '')

        if table[b] == 0 or table[b] == -1:
            return 0
        
        elif table[b] == key:
            return table[b]
        
        else:
            i += 1

    # hash Table이 꽉 차 있는데, 값이 없다.
    return 0

def delete(key):
    v = hashFn(key)
    i = 0
    
    while i < M:
        b = getLinear(v, i)
        #b = getQuadratic(v, i)
        #b = getDouble(v, i, key)
        
        print('[%d] '%table[b], end = '')
        
        if table[b] == 0:
            print('No Key to delete')
            return

        elif table[b] == key:
            table[b] = -1 # 처음부터 비어있던 곳이 아니야! 두 가지의 상황 표현 in 개방주소법..
            return

        else:
            i += 1

def display():
    print()
    print("Bucket   Key")
    print('============')
    
    for i in range(M):
        print('HT[%2d] : %2d'%(i, table[i]))

if __name__ == "__main__":
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data:
        print('h(%2d) = %2d'%(d, hashFn(d)), end = ' ')
        insert(d)
        print(table)
    
    display()
    print()
    
    delete(60)
    print()
    print('Search(60) ---> ', search(60))
    print('Search(46) ---> ', search(46))
    #print('Search(39) ---> ', search(39))
    