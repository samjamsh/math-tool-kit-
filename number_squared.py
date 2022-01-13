try:
    valor = 0 # define the variable
    while True:
        numero = input("raiz: ")
        try:
            numero = int(numero)           
            break

        except:
            pass

    valor = numero*numero # number squared

    print(f"{numero} ao quadrado é {valor}")

except:
    pass
