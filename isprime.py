#ACTIVIDAD FORMATIVA 5
#MATEMATICA DISCRETA 1 - 10
#FERNANDO RUIZ - 23065
#NINA NÁJERA - 231088
#--

import time

def prime_test1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n):
        if i in not_prime:
            continue

        for j in range(i * 2, n, i):
            not_prime.add(j)
        primes.append(i)
    return primes

def first_div(n):
    prime_list = criba(int(n ** 0.5) + 1)

    for i in prime_list:
        if n % i == 0:
            return i  
    return True

# MAIN
while True:
    try:
        a = int(input("Ingrese un número entero positivo: "))
        if a > 0:
            break
        else:
            print("No es un numero entero positivo.")
    except ValueError:
        print("Solo numeros.")

start_time = time.time()

result = first_div(a)
if result is True:
    print(f"El numero {a} es primo.")
else:
    print(f"El numero {a} no es primo, porque lo divide {result}.")

end_time = time.time()
print("Se ejecuto en " + str(end_time - start_time) + " segundos.")
