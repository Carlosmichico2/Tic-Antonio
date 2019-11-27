def pajarita ():
    filas = int(input("Filas: \n"))
    filas = filas/2
    for i in range (1,filas+1):
        if i <=filas:
            print ("*"*(i)+" "*((filas-2*i))+"*"*((i)))
        elif i>filas:
            print("*"*((filas-i))+" "*((filas-2*(filas-i)))+"*"*((filas-i)))

pajarita()
