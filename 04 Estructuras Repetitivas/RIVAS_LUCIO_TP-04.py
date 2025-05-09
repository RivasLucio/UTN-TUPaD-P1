import random

#### EJERCICIO 1 ####
for i in range(0, 101):
    print(f"{i}")
#### EJERCICIO 2 ####
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(numero))
print(f"El número ingresado tiene {cantidad_digitos} dígitos.")
#### EJERCICIO 3 ####
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
if valor1 > valor2:
    valor1, valor2 = valor2, valor1
suma = sum(range(valor1 + 1, valor2))
print(f"La suma de los números enteros comprendidos entre {valor1} y {valor2} es: {suma}")

#### EJERCICIO 5 ####
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
    else:
        print("Número incorrecto, intenta nuevamente.")

#### EJERCICIO 6 #### 
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
#### EJERCICIO 7 #### 
numero = int(input("Ingrese un número entero positivo: "))
if numero >= 0:
    suma = sum(range(numero + 1))
    print(f"La suma de todos los números entre 0 y {numero} es: {suma}")
else:
    print("El número ingresado no es positivo.")


#### EJERCICIO 10 ####
numero = int(input("Ingrese un número entero: "))
numero_invertido = int(str(numero)[::-1])
print(f"El número invertido es: {numero_invertido}")