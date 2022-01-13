a,b=0,0
try:
    while True:
        a = input("dividendo: ") # first number

        b = input("divisor: ") # second number

        try:
            a = int(a)
            b = int(b)
            break

        except:
            pass
        

    c = a/b # the division
    d = int(c) # set the value to int
    e = d*b # value * second number
    f = a-e # first number - e

    result = f # rest
    value = c
    print("O resto é",result,"e o quociente é:",int(value))

except KeyboardInterrupt:
    pass
