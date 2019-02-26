#Autor : Henrique Wippel Parucker da Silva
#Para compilar basta usar o python 3 e digitar o nome do arquivo
#Obs: Código usa a biblioteca sympy que não é nativa
from sympy import *
x = Symbol('x')
if __name__ == '__main__':
    a = input("Digite o A do intervalo para a função f(x) = x²-2:  ")
    b = input("Digite o B do intervalo para a função f(x) = x²-2:  ")
    f = "x**2 - 2"
    fx = sympify(f) #Transforma string em uma função
    fa = fx.evalf(subs={x : a}) #Substitui o intervalo A na função e resolve ela
    fb = fx.evalf(subs={x : b}) #Substitui o intervalo B na função e resolve ela
    p1 = a
    p2 = b
    v = input("Digite o numero de interações: ")
    pn = a
    pn1 = b

    print("-----------------------")
    for n in range (0,int(v)): #Looping para resolver o número de interações digitado pelo usuário
        print ("n = ", n+1)
        print ("pn =", pn)
        print ("pn+1 = ", pn1)
        fpn = fx.evalf(subs={x:pn}) #Resolve f(pn)
        print ("f(pn) = ", fpn)
        fpn1 = fx.evalf(subs={x:pn1}) #Resolve f(pn+1)
        print("f(pn+1) = ", fpn1)
        a = fpn1 - fpn
        b = float(pn1) - float(pn)
        c = fpn*b
        pn2= float(pn)- c/a #Resolve pn+2 = pn - (f(pn)*(pn+1 - pn))/(f(pn+1)-f(pn))
        print ("pn+2 =", (pn2))
        print ("-----------------------")
        pn = pn1
        pn1 = pn2
        #print ("novo pn = ", pn)
        #print ("novo pn1 = ", pn1)
