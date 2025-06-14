import math

# --- Ejercicio 1: Factorial Recursivo ---
def factorial_recursivo(numero):
    """
    Calcula el factorial de un número de forma recursiva.

    Args:
        numero (int): El número entero no negativo.

    Returns:
        int: El factorial del número.
    """
    if numero == 0:  # Caso base: El factorial de 0 es 1
        return 1
    else:  # Caso recursivo: n * factorial(n-1)
        return numero * factorial_recursivo(numero - 1)

# --- Ejercicio 2: Serie de Fibonacci Recursiva ---
def fibonacci_recursivo(pos):
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada de forma recursiva.

    Args:
        pos (int): La posición en la serie de Fibonacci (>= 0).

    Returns:
        int: El valor de Fibonacci en esa posición.
    """
    if pos == 0:  # Caso base 1: F(0) es 0
        return 0
    elif pos == 1:  # Caso base 2: F(1) es 1
        return 1
    else:  # Caso recursivo: F(n) = F(n-1) + F(n-2)
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

# --- Ejercicio 3: Potencia Recursiva ---
def potencia_recursiva(base, exponente):
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.

    Args:
        base (int/float): El número base.
        exponente (int): El exponente (entero no negativo).

    Returns:
        int/float: El resultado de base^exponente.
    """
    if exponente == 0:  # Caso base: Cualquier número elevado a 0 es 1
        return 1
    elif exponente < 0: # Manejo de exponentes negativos (opcional, no explícito en la fórmula dada,
                        # pero una buena práctica para una función de potencia completa)
        return 1 / potencia_recursiva(base, -exponente)
    else:  # Caso recursivo: n^m = n * n^(m-1)
        return base * potencia_recursiva(base, exponente - 1)

# --- Ejercicio 4: Decimal a Binario Recursivo ---
def decimal_a_binario_recursivo(numero_decimal):
    """
    Convierte un número entero positivo en base decimal a su representación en binario
    como una cadena de texto, de forma recursiva.

    Args:
        numero_decimal (int): El número decimal entero positivo.

    Returns:
        str: La representación binaria del número.
    """
    if numero_decimal == 0:  # Caso base: La representación binaria de 0 es "0"
        return "0"
    elif numero_decimal == 1: # Caso base: La representación binaria de 1 es "1"
        return "1"
    else:  # Caso recursivo: (numero_decimal // 2) en binario + str(numero_decimal % 2)
        return decimal_a_binario_recursivo(numero_decimal // 2) + str(numero_decimal % 2)

# --- Ejercicio 5: Palíndromo Recursivo ---
def es_palindromo(palabra):
    """
    Verifica si una cadena de texto es un palíndromo de forma recursiva.
    La palabra debe venir sin espacios ni tildes.

    Args:
        palabra (str): La cadena de texto a verificar.

    Returns:
        bool: True si es un palíndromo, False en caso contrario.
    """
    if len(palabra) <= 1:  # Caso base: Una cadena vacía o de un solo carácter es un palíndromo
        return True
    else:  # Caso recursivo: Compara los extremos y verifica el subproblema central
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1]) # Llama con la subcadena sin el primer y último carácter
        else:
            return False

# --- Ejercicio 6: Suma de Dígitos Recursiva ---
def suma_digitos(n):
    """
    Calcula la suma de todos los dígitos de un número entero positivo de forma recursiva.

    Args:
        n (int): El número entero positivo.

    Returns:
        int: La suma de sus dígitos.
    """
    if n < 10:  # Caso base: Si el número tiene un solo dígito, la suma es el propio número
        return n
    else:  # Caso recursivo: Último dígito + suma de los dígitos del resto del número
        return (n % 10) + suma_digitos(n // 10)

# --- Ejercicio 7: Contar Bloques de Pirámide Recursiva ---
def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide,
    donde el nivel más bajo tiene 'n' bloques y cada nivel superior tiene uno menos.

    Args:
        n (int): El número de bloques en el nivel más bajo (entero positivo).

    Returns:
        int: El total de bloques en la pirámide.
    """
    if n == 0:  # Caso base: No hay bloques si el nivel base es 0
        return 0
    else:  # Caso recursivo: n + bloques de la pirámide con n-1 en la base
        return n + contar_bloques(n - 1)

# --- Ejercicio 8: Contar Dígito Recursiva ---
def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito específico dentro de un número entero positivo.

    Args:
        numero (int): El número entero positivo a analizar.
        digito (int): El dígito a contar (entre 0 y 9).

    Returns:
        int: La cantidad de veces que aparece el dígito.
    """
    if numero == 0:  # Caso base: Si el número se reduce a 0, no hay más dígitos que contar
        return 0
    else:
        # Verificar si el último dígito del número es el dígito buscado
        if (numero % 10) == digito:
            return 1 + contar_digito(numero // 10, digito) # Suma 1 y sigue con el resto del número
        else:
            return contar_digito(numero // 10, digito) # No suma y sigue con el resto del número


# ====================================================================
# Programa Principal para probar las funciones
# ====================================================================
print("----- Práctico 11: Aplicación de la Recursividad -----")

# Ejercicio 1: Factorial
print("\n--- Ejercicio 1: Factorial Recursivo ---")
try:
    num_factorial_max = int(input("Ingresa un número entero positivo para calcular factoriales hasta él: "))
    if num_factorial_max < 0:
        print("Por favor, ingresa un número positivo o cero.")
    else:
        for i in range(1, num_factorial_max + 1):
            print(f"El factorial de {i} es: {factorial_recursivo(i)}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

# Ejercicio 2: Fibonacci
print("\n--- Ejercicio 2: Serie de Fibonacci Recursiva ---")
try:
    pos_fibonacci_max = int(input("Ingresa la posición máxima para la serie de Fibonacci: "))
    if pos_fibonacci_max < 0:
        print("La posición debe ser un número no negativo.")
    else:
        print("Serie de Fibonacci hasta la posición", pos_fibonacci_max, ":")
        for i in range(pos_fibonacci_max + 1):
            print(f"F({i}) = {fibonacci_recursivo(i)}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

# Ejercicio 3: Potencia
print("\n--- Ejercicio 3: Potencia Recursiva ---")
try:
    base_pot = float(input("Ingresa la base para la potencia: "))
    exp_pot = int(input("Ingresa el exponente (entero no negativo): "))
    if exp_pot < 0:
        print("El exponente debe ser un entero no negativo para este ejercicio (o se manejará como 1/base^|exponente|).")
    resultado_potencia = potencia_recursiva(base_pot, exp_pot)
    print(f"{base_pot} elevado a la {exp_pot} es: {resultado_potencia}")
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números válidos.")

# Ejercicio 4: Decimal a Binario
print("\n--- Ejercicio 4: Decimal a Binario Recursivo ---")
try:
    num_decimal_bin = int(input("Ingresa un número entero positivo en decimal para convertirlo a binario: "))
    if num_decimal_bin < 0:
        print("Por favor, ingresa un número entero positivo.")
    elif num_decimal_bin == 0:
        print(f"El número {num_decimal_bin} en binario es: 0") # Manejo especial para 0, ya que la recursión devuelve "0" si el inicial es 0
    else:
        # Para el caso 0, la función base devuelve "0".
        # Si el usuario ingresa 0, la función devuelve "0".
        # Si la recursión llega a 0, devuelve "0" y se concatena.
        # Por ejemplo, decimal_a_binario_recursivo(10) llama a decimal_a_binario_recursivo(5) + "0", etc.
        # hasta decimal_a_binario_recursivo(1) + "0". El 1 devuelve "1".
        # Luego se construye hacia atrás.
        binario_result = decimal_a_binario_recursivo(num_decimal_bin)
        print(f"El número {num_decimal_bin} en binario es: {binario_result.lstrip('0') or '0'}")
        # .lstrip('0') or '0' para manejar el caso de que la función retorne "0" para 0,
        # y evitar "01010" si la implementación de la función recursiva no maneja el 0 inicial.
        # Mi implementación actual lo hace bien, así que lstrip('0') es solo por si acaso
        # para evitar un "0" inicial si se da el caso de que el primer dígito que se genera es 0
        # antes de un 1, lo cual es incorrecto para numeros > 0.
        # En mi función, el 0 solo se devuelve para la entrada 0. Para otros,
        # el 0 inicial se construye solo si el número es pequeño y termina en 0.
        # Por ejemplo, si num_decimal_bin es 2, el binario es "10".
        # La recursión para 2 es decimal_a_binario_recursivo(1) + "0" -> "1" + "0" -> "10".
        # No hay ceros iniciales incorrectos.
        # El .lstrip('0') or '0' es principalmente para números como 0.
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero positivo.")

# Ejercicio 5: Palíndromo
print("\n--- Ejercicio 5: Palíndromo Recursivo ---")
palabra_test = input("Ingresa una palabra para verificar si es un palíndromo (sin espacios ni tildes): ").lower()
if es_palindromo(palabra_test):
    print(f"'{palabra_test}' es un palíndromo.")
else:
    print(f"'{palabra_test}' NO es un palíndromo.")

# Ejercicio 6: Suma de Dígitos
print("\n--- Ejercicio 6: Suma de Dígitos Recursiva ---")
try:
    num_suma_digitos = int(input("Ingresa un número entero positivo para sumar sus dígitos: "))
    if num_suma_digitos < 0:
        print("Por favor, ingresa un número entero positivo.")
    else:
        resultado_suma_digitos = suma_digitos(num_suma_digitos)
        print(f"La suma de los dígitos de {num_suma_digitos} es: {resultado_suma_digitos}")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

# Ejercicio 7: Contar Bloques
print("\n--- Ejercicio 7: Contar Bloques de Pirámide Recursiva ---")
try:
    bloques_base = int(input("Ingresa el número de bloques en el nivel más bajo de la pirámide: "))
    if bloques_base < 0:
        print("El número de bloques debe ser no negativo.")
    else:
        total_bloques = contar_bloques(bloques_base)
        print(f"Para una pirámide con {bloques_base} bloques en la base, se necesitan un total de {total_bloques} bloques.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")

# Ejercicio 8: Contar Dígito
print("\n--- Ejercicio 8: Contar Dígito Recursiva ---")
try:
    num_contar = int(input("Ingresa un número entero positivo para contar un dígito: "))
    dig_buscar = int(input("Ingresa el dígito (0-9) a buscar: "))

    if num_contar < 0 or not (0 <= dig_buscar <= 9):
        print("Por favor, ingresa un número positivo y un dígito entre 0 y 9.")
    else:
        # Caso especial para 0 y buscar 0
        if num_contar == 0 and dig_buscar == 0:
            print(f"El dígito {dig_buscar} aparece 1 vez en {num_contar}.")
        elif num_contar == 0 and dig_buscar != 0:
             print(f"El dígito {dig_buscar} aparece 0 veces en {num_contar}.")
        else:
            apariciones = contar_digito(num_contar, dig_buscar)
            print(f"El dígito {dig_buscar} aparece {apariciones} veces en {num_contar}.")
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números enteros válidos.")

print("\n----- Fin del Práctico 11 -----")