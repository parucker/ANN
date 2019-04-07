#Autor : Henrique Wippel Parucker da Silva
#Para compilar basta usar o python 3 e digitar o nome do arquivo
#Obs: Código usa a biblioteca sympy que não é nativa
from sympy import *
x = Symbol('x')

def metodoSecante (pn,pn1,fx):
    fpn = fx.evalf(subs={x:pn}) #Resolve f(pn)
    fpn1 = fx.evalf(subs={x:pn1}) #Resolve f(pn+1)
    a = fpn1 - fpn
    b = float(pn1) - float(pn)
    c = fpn*b
    pn2= float(pn)- c/a #Resolve pn+2 = pn - (f(pn)*(pn+1 - pn))/(f(pn+1)-f(pn))
    return float(pn2)

if __name__ == '__main__':
    a = input("Digite o A do intervalo para a função f(x) = x²-2:  ")
    b = input("Digite o B do intervalo para a função f(x) = x²-2:  ")
    f = "x**2 - 2"
    fx = sympify(f) #Transforma string em uma função
    fpn = fx.evalf(subs={x : a}) #Substitui o intervalo A na função e resolve ela
    fpnMais1 = fx.evalf(subs={x : b}) #Substitui o intervalo B na função e resolve ela
    v = int(input("Digite o numero de interações: "))
    pn = float(a)
    pnMais1 = float(b)
    print("-------------------------")
    if(fpn*fpnMais1<0):
        pnMais2 = metodoSecante(pn,pnMais1,fx) #Calcula o primeiro pn+2
        fpnMais2 = fx.evalf(subs={x : pnMais2}) #calcula o primiero f(pn+2)
    if(fpnMais2==0):
        print("Voce achou a raiz")
    n=0
    print("n: ",n+1)
    print("pn: ",pn)
    print ("pn+1: ", pnMais1)
    print("f(pn): ",fpn)
    print("f(pn+1): ",fpnMais1)
    print ("pn+2: ", pnMais2)
    print("f(pn+2)",fpnMais2)
    print("-------------------------")
    for n in range(1,v):
            fafc = fpn*fpnMais2 #f(a)*f(c) para mais tarde ver se é menor que 0
            fbfc = fpnMais1*fpnMais2 #f(b)*f(c) para mais tarde ver se é menor que 0
            if(fafc<0):
                pn = pnMais2 #Substitui pn por pn+2
                fpn = fx.evalf(subs={x : pn}) #resolve f(pn)
                pnMais2 = metodoSecante(pn,pnMais2,fx)   #Entra no metodo da descante para achar pn+2, passando pn e pn+2 para a função
                fpnMais2 = fx.evalf(subs={x : pnMais2})  #resolve f(pn+2)
            if(fbfc<0):
                pn = pnMais2 #Substitui pn por pn+2
                fpn = fx.evalf(subs={x : pn})       #resolve f(pn)
                pnMais2 = metodoSecante(pnMais1,pnMais2,fx) #Entra no metodo da descante para achar pn+2, passando pn+1 e pn+2 para a função
                fpnMais2 = fx.evalf(subs={x : pnMais2}) #resolve f(pn+2)
            print("n: ",n+1)
            print("pn: ",pn)
            print ("pn+1: ", pnMais1)
            print("f(pn): ",fpn)
            print("f(pn+1): ",fpnMais1)
            print ("pn+2: ", pnMais2)
            print("f(pn+2)",fpnMais2)
            print("-------------------------")
