from sympy import *
x = Symbol('x')
if __name__ == '__main__':
    a = input("Digite o A do intervalo para a função f(x) = x²-2:  ")
    b = input("Digite o B do intervalo para a função f(x) = x²-2:  ")
    f = "x**2 - 2"
    fx = sympify(f) #Transforma string em uma função
    fa = fx.evalf(subs={x : a}) #Substitui o intervalo A na função e resolve ela
    fb = fx.evalf(subs={x : b}) #Substitui o intervalo B na função e resolve ela
    v = int(input("Digite o numero de interações: "))
    if(fa*fb>0):
        print("f(a)*f(b) não satifaz o intervalo")
    a1 = float(a)
    b1= float(b)
    m1=(a1+b1)/2
    fm = fx.evalf(subs={x : m1})
    for n in range (0,v):
        fa = fx.evalf(subs={x : a1}) #Substitui o intervalo A na função e resolve ela
        fb = fx.evalf(subs={x : b1}) #Substitui o intervalo B na função e resolve ela
        print("---------------------------")
        print("k: ", n+1)
        print("ak: ",a1)
        print("bk: ",b1)
        print("f(ak):" ,fa)
        print("f(mk): ", fm)
        print("f(bk): ",fb)
        if((fm*fb)<0):
            a1=m1
            #m1 = (a1+b1)/2
        else:
            b1=m1
            #m1 = (a1+b1)/2
        print("mk: ",m1)
        m1=(a1+b1)/2
        fm = fx.evalf(subs={x : m1}) #Substitui o intervalo B na função e resolve ela
