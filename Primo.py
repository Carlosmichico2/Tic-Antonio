def primos ():
    numero=input ("inserta un numero=")
    for i in range(2,numero):
        if(numero%i==0):
            print"Es primo"
        else:
            print"no es primo"

primos()
