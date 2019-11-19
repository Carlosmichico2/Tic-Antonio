#crea una pirámide
def piramide():
    filas=input("dime la altura en pisos: ")
    espacios=' '
    asteriscos='*'
    for i in range(filas):
        for nespacios in range(1,filas-i-1):
            espacios=espacios+' '
        for nasteriscos in range(1,2*i):
            asteriscos=asteriscos+'*'
        #escribo de golpe toda la fila
        print espacios + asteriscos
        espacios=' '
        asteriscos='*'
        #Paso a la siguiente fila
        

piramide()        
