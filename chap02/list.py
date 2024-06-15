L1=[3,5,7,9]
L2=['A','B','C','D']
print(L1)
print('L1[1]=',L1[1])
L2[2]='F'
print(L2)
L1.append(11)

print(L1)
print(L1.pop())
print(L1)
L2.extend(L1) # type: ignore
print(L1)
print(L2)

print(L2.count('B'))
L1.insert(2,1)
print(L1)