map={'apple':'���','peach':'������','banana':'�ٳ���','ship':'��'}
print(map)
for key in map:
    print("%s => %s" %(key,map[key]))
    
map['grape']='����'
print(map)

map.update({'orange':'������','mandarin':'���ٸ�'})
print(map)

print(map.keys())
print(map.values()) ##??? ���� ��� ??? ????? ! ! !