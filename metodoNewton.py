#Autor : Henrique Wippel Parucker da Silva
#Para compilar basta usar o python 3 e digitar o nome do arquivo
#Obs: Código usa a biblioteca sympy que não é nativa
from sympy import *
x = Symbol('x')
if __name__ == '__main__':
    a = input("Digite o P1 do intervalo para a função f(x) = x²-2:  ")
    f = "x**2 - 2"
    fx = sympify(f) #Transforma string em uma função
    fa = fx.evalf(subs={x : a}) #Substitui o intervalo A na função e resolve ela
    v = int(input("Digite o numero de interações: "))
    fl = fx.diff(x) #Realiza a derivada da função
    print("Derivada da função: ",fl)
    pn = float(a)
    print("-------------------------")
    for n in range(0,v):
        fp = fx.evalf(subs={x : pn})
        flp = fl.evalf(subs={x : pn})
        pnMais1 = pn - (fp/flp)
        print("n: ",n+1)
        print("pn: ",pn)
        print("f(pn): ",fp)
        print("f'(pn): ", flp)
        print("pn+1: ",pnMais1)
        pn = pnMais1
        print("-------------------------")
