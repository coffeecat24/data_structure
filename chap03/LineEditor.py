from ArrayListClass import ArrayList

list=ArrayList()
while True:
    command = input('[select menu] i-input, d-delete, r-read, p-print, l-load, s-save, q-quit : ')
    if command=='i':
        pos = int(input('입력 행 번호 : '))
        str=input('입력 행 내용 : ')
        list.insert(pos,str)
    elif command=='d':
        pos=int(input('삭제 행 번호 : '))
        list.delete(pos)
    elif command=='r':
        pos=int(input('변경 행 번호 : '))
        str=input('변경 행 내용 : ')
        list.replace(pos,str)
    elif command=='p':
        print('Line Editor')
        for line in range(list.size):
            print('[%d]'%line,end=' ')
            print(list.getEntry(line))
        print()
        
    elif command=='l':
        filename='chap03/test.txt'
        infile=open(filename,'r')
        lines =infile.readlines()
        for line in lines:
            list.insert(list.size,line.rstrip('\n'))
        infile.close()
        
    elif command=='s':
        filename='chap03/test.txt'
        outfile=open(filename,'w')
        len=list.size
        
        for i in range (len):
            outfile.write(list.getEntry(i)+'\n') #type:ignore
        outfile.close()
        
    elif command=='q':
        exit()    