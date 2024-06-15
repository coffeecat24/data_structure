from ArrayStack import ArrayStack

def evalPostfix(expr):
    S=ArrayStack(100)
    for token in expr:
        if token in '+-*/':
            val2=S.pop()
            val1=S.pop()
            if token =='+': S.push(val1+val2) #type:ignore
            elif token== '-': S.push(val1-val2) #type:ignore
            elif token== '*': S.push(val1*val2) #type:ignore
            elif token== '/': S.push(val1/val2) #type:ignore
        else:
            S.push(float(token))
    return S.pop()

if __name__=='__main__':
    str = '8 2 / 3 - 3 2 * +'
    expr=str.split()
    
    print(str,'-->',evalPostfix(expr))