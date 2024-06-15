from ArrayStack import ArrayStack

def precedence(op):
    if(op=='(' or op==')'): return 0
    elif(op=='+' or op=='-'): return 1
    elif(op=='*' or op=='/'): return 2
    else: return -1

def infixToPostfix(expr):
    S=ArrayStack(100)
    postfix=[]
    
    for term in expr:
        if term in '(':
            S.push('(')
        elif term in ')':
            while not S.isEmpty():
                op=S.pop()
                if op=='(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not S.isEmpty():
                op=S.peek()
                if(precedence(term)<=precedence(op)):
                    postfix.append(op)
                    S.pop()
                else: break
            S.push(term)
        else:
            postfix.append(term)
            
    while not S.isEmpty():
        postfix.append(S.pop())
        
    return postfix


if __name__=='__main__':
    infix=input('Input Infix Expr : ')
    expr = infix.split()
    postfix=infixToPostfix(expr)
    
    print(postfix)