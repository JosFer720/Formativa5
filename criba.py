#ACTIVIDAD FORMATIVA 5
#MATEMATICA DISCRETA 1 - 10
#FERNANDO RUIZ - 23065
#NINA NÁJERA - 231088
#DIEGO LÓPEZ - 23747

import time

def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n):
        if i in not_prime:
            continue

        for j in range(i*2, n, i):
            not_prime.add(j)
        primes.append(i)
    return primes

def main(n):
    prime_list = criba(int(n**0.5))

    for i in prime_list:
        if n % i == 0:
            return False
    return True

while True:
    try:
        a = int(input("Ingrese un numero entero positivo: "))
        if a > 0:
            break
        else:
            print("No es un numero entero positivo.")
    except ValueError:
        print("Solo numeros,")

start_time = time.time()
print("¿Es primo?", main(a))
print("Criba de Eratostenes hasta", a, ":", criba(a))
end_time = time.time()
print("Se ejecutó en " + str(end_time - start_time) + " segundos.")