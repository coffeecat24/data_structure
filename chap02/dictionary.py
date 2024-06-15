map={'apple':'사과','peach':'복숭아','banana':'바나나','ship':'배'}
print(map)
for key in map:
    print("%s => %s" %(key,map[key]))
    
map['grape']='포도'
print(map)

map.update({'orange':'오렌지','mandarin':'만다린'})
print(map)

print(map.keys())
print(map.values()) ##??? 개는 기억 ??? ????? ! ! !