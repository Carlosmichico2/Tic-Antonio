#En este programa le pedimos al usuario que teclee los coeficientes de un polinomio
import math 
def ecuacion():
    print "introduzca los coeficientes del polinomio"
    print "A*x^2+B*x+C=0"
    a=input("A= ")
    b=input("B= ")
    c=input("C= ")
    radicando=b*b-4*a*c
    if (radicando>0):
        raiz1=(-b+math.sqrt(radicando))/(2*a)
        raiz2=(-b-math.sqrt(radicando))/(2*a)
        print "primera solucion= "
        print raiz1
        print "segunda solucion= "
        print raiz2
    else:
        print "esta ecuacion no tiene solucion real"

ecuacion()
     
