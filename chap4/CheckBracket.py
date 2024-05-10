from ArrayStack import ArrayStack

def checkbracktets(str):
    S=ArrayStack(100)
    
    for c in str:
        if c=='(' or c=='[' or c=='{':
            S.push(c)
        elif c==')' or c=='}' or c==']':
            if S.isEmpty():
                return False
            else:
                left=S.pop()
            if (c==']'and left!='[') or \
                (c=='}' and left!='{') or\
                (c==')' and left!='('):
                    return False
    return S.isEmpty()

if __name__=='__main__':
    s1='{ A[(i+1)]=0}'
    s2='if((i==0)&&(j==0)'
    s3='A[(i+1])=0'
    
    print(s1,'-->',checkbracktets(s1))
    print(s2,'-->',checkbracktets(s2))
    print(s3,'-->',checkbracktets(s3))
    
    filename='cfile.txt'
    inFile=open(filename,'r')
    str=inFile.read()
    inFile.close()
    
    print(filename,'-->',checkbracktets(str))