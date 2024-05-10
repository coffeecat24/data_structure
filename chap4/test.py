from EvalPostfix import evalPostfix
from infixToPostfix import infixToPostfix

infix=input('Input Infix Expr : ')
expr = infix.split()
print(expr,'=',evalPostfix(infixToPostfix(expr)))