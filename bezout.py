#ACTIVIDAD FORMATIVA 5
#MATEMATICA DISCRETA 1 - 10
#FERNANDO RUIZ - 23065
#NINA NÁJERA - 231088
#DIEGO LÓPEZ - 23747

import numpy as np
import time
from functools import reduce

def euclidean(a, b):
    cocientes = []
    if b > a:
        a, b = b, a
    while b != 0:
        cocientes.append(a // b)
        a, b = b, a % b
        
        
    return cocientes

def bezout(cocientes: list):
    matrices = []
    
    for i in cocientes:
        matriz = np.array([[i, 1], [1, 0]])
        matrices.append(matriz)
        
    matriz_final = reduce(np.dot, matrices)
    signo = (-1)**(len(cocientes) - 1)
    
    y,x = (matriz_final[0][1]) * signo,( matriz_final[1][1] * -1) * signo
    
    return x,y 
    

a = int(input("Ingrese un numero entero positivo a: "))
b = int(input("Ingrese un numero entero positivo b: "))

if a > 0 and b > 0: 
    start_time = time.time()
    cocientes = euclidean(a, b)
    x,y = bezout(cocientes)
    
    print(f"Los coeficientes de Bezout de {a} y {b} son: {x} y {y}")
    end_time = time.time()
    print("Se ejecuto en " + str(end_time - start_time) + " segundos.")