#ACTIVIDAD FORMATIVA 5
#ACTIVIDAD FORMATIVA 5
#MATEMATICA DISCRETA 1 - 10
#FERNANDO RUIZ - 23065
#NINA NÁJERA - 231088
#DIEGO LÓPEZ - 23747

import time

def euclidean(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a  

# MAIN
while True: 
    try:
        a = int(input("Ingrese un numero entero positivo a: "))
        b = int(input("Ingrese un numero entero positivo b: "))
        if a > 0 and b > 0: 
            break
        else:
            print("Ambos numeros deben ser enteros positivos.")
    except ValueError:
        print("Solo se permiten numeros enteros positivos.")

start_time = time.time()
mcd = euclidean(a, b) 
print("El mcd de", a, "y", b, "es", mcd)
end_time = time.time()
print("Se ejecuto en " + str(end_time - start_time) + " segundos.")


