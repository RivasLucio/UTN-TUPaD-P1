import math

# --- Actividad 1 ---
def imprimir_hola_mundo():
    print("Hola Mundo!")

# --- Actividad 2 ---
def saludar_usuario(nombre):
 
    return f"Hola {nombre}!"

# --- Actividad 3 ---
def informacion_personal(nombre, apellido, edad, residencia):
  
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# --- Actividad 4 ---
def calcular_area_circulo(radio):
 
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    
    return 2 * math.pi * radio

# --- Actividad 5 ---
def segundos_a_horas(segundos):
   
    return segundos / 3600

# --- Actividad 6 ---
def tabla_multiplicar(numero):
  
    print(f"\n--- Tabla de multiplicar del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("---------------------------------")

# --- Actividad 7 ---
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None # Manejo de división por cero
    return (suma, resta, multiplicacion, division)

# --- Actividad 8 ---
def calcular_imc(peso, altura):
   
    if altura > 0:
        return peso / (altura ** 2)
    else:
        return None # Evitar división por cero

# --- Actividad 9 ---
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# --- Actividad 10 ---
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# ====================================================================
# Programa Principal
# Aquí se llaman las funciones y se interactúa con el usuario
# ====================================================================

print("--- Actividad 1: Saludo Simple ---")
imprimir_hola_mundo()
print("-" * 30 + "\n")

print("--- Actividad 2: Saludo Personalizado ---")
nombre_usuario = input("Por favor, ingresa tu nombre para el saludo: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)
print("-" * 30 + "\n")

print("--- Actividad 3: Información Personal ---")
nombre_info = input("Ingresa tu nombre: ")
apellido_info = input("Ingresa tu apellido: ")
edad_info = int(input("Ingresa tu edad: "))
residencia_info = input("Ingresa tu residencia: ")
informacion_personal(nombre_info, apellido_info, edad_info, residencia_info)
print("-" * 30 + "\n")

print("--- Actividad 4: Área y Perímetro del Círculo ---")
try:
    radio_circulo = float(input("Ingresa el radio del círculo: "))
    if radio_circulo >= 0:
        area = calcular_area_circulo(radio_circulo)
        perimetro = calcular_perimetro_circulo(radio_circulo)
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
    else:
        print("El radio no puede ser negativo.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para el radio.")
print("-" * 30 + "\n")

print("--- Actividad 5: Segundos a Horas ---")
try:
    segundos_input = int(input("Ingresa una cantidad de segundos: "))
    if segundos_input >= 0:
        horas_result = segundos_a_horas(segundos_input)
        print(f"{segundos_input} segundos equivalen a {horas_result:.2f} horas.")
    else:
        print("La cantidad de segundos no puede ser negativa.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero para los segundos.")
print("-" * 30 + "\n")

print("--- Actividad 6: Tabla de Multiplicar ---")
try:
    numero_tabla = int(input("Ingresa un número para ver su tabla de multiplicar (del 1 al 10): "))
    tabla_multiplicar(numero_tabla)
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
print("-" * 30 + "\n")

print("--- Actividad 7: Operaciones Básicas ---")
try:
    num1_ops = float(input("Ingresa el primer número para las operaciones: "))
    num2_ops = float(input("Ingresa el segundo número para las operaciones: "))
    suma, resta, multiplicacion, division = operaciones_basicas(num1_ops, num2_ops)

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    if division is not None:
        print(f"División: {division}")
    else:
        print("No se puede dividir por cero.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos.")
print("-" * 30 + "\n")

print("--- Actividad 8: Cálculo del IMC ---")
try:
    peso_imc = float(input("Ingresa tu peso en kilogramos: "))
    altura_imc = float(input("Ingresa tu altura en metros: "))
    if peso_imc > 0 and altura_imc > 0:
        imc_resultado = calcular_imc(peso_imc, altura_imc)
        if imc_resultado is not None:
            print(f"Tu Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")
        else:
            print("No se puede calcular el IMC con altura cero.")
    else:
        print("El peso y la altura deben ser valores positivos.")
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números válidos para peso y altura.")
print("-" * 30 + "\n")

print("--- Actividad 9: Celsius a Fahrenheit ---")
try:
    celsius_temp = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit_temp = celsius_a_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C equivalen a {fahrenheit_temp:.2f}°F.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para la temperatura.")
print("-" * 30 + "\n")

print("--- Actividad 10: Calcular Promedio ---")
try:
    p1 = float(input("Ingresa el primer número para el promedio: "))
    p2 = float(input("Ingresa el segundo número para el promedio: "))
    p3 = float(input("Ingresa el tercer número para el promedio: "))
    promedio_final = calcular_promedio(p1, p2, p3)
    print(f"El promedio de {p1}, {p2} y {p3} es: {promedio_final:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa números válidos.")
print("-" * 30 + "\n")

print("¡Todas las actividades completadas!")