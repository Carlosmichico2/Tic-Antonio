# -*- coding: cp1252 -*-
def ejercicio6():
    print "¿que dos numeros quieres?"
    a=input("a= ")
    b=input("b= ")
    print "Elige:sumar(S),restar(R),multiplicacion(M) o division(D)"
    operacion=raw_input("letra= ")
    if (operacion=="S"):
        print ("Suma= "),a+b
    if (operacion=="R"):
        print("Resta= "),a-b
    if (operacion=="M"):
        print("Multiplicar= "),a*b
    if (operacion=="D"):
        print ("Division= "),a/b
ejercicio6()
