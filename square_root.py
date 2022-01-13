try:
    valor = 0
    while True:
        valor = input("raiz: ")
        try:
            valor = int(valor)           
            break

        except:
            pass

    x,y = 1,0
    import sys; sys.exit(f"Resultado: {valor}") if valor==1 or valor==0 else print(end='');

    while x <= valor:
        y+=1
        x+=0.10
        x=x-0.04
        if str(valor) == str(x*x)[0]: # if the result is an int
            print(f"A raiz quadrada de {float(valor)} e {str(x)[:]}")
            state = True
            modo = 1
            sys.exit()
    # if the result is a float
        elif y*y == valor:
            print("A raiz quadrada e",y)
            sys.exit()

        else:
            pass 

except KeyboardInterrupt as ctrlc:
    pass

