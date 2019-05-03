import random

a = random.randint(1, 100)
c = 0
for i in range(1, 11):
    b = int(input("Ingrese un valor entre 1 y 100: "))
    if a == b:
        print("Crack!! le pegaste en ", i,"intentos!")
        c = 1
        break
    elif a < b:
        print("El valor ingresado es mayor al incognita")
    else:
        print("El valor ingresado es menor al incognita")
if c != 1:
    print("Sos un muerto!! no le pegaste ni una vez")




