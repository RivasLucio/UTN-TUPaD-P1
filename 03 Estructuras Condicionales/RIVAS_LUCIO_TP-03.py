##### ejercicio 1 ####
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
##### ejercicio 2 ####
nota = float(input("Introduce tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Reprobado") 
##### ejercicio 3 ####
numero_par=int(input("Introduce un número: "))
if numero_par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

##### ejercicio 4 ####
edad_ = int(input("Introduce tu edad: "))
if edad_ < 12:
    print("Eres un niño/a.")
elif 12 <= edad_ < 18:
    print("Eres un adolescente.")
elif 18 <= edad_ < 30:
    print("Eres un adulto/a joven.")
else:
    print("Eres un adulto/a.")
##### ejercicio 5 ####
contraseña= input("Introduce una contraseña :")
if  8 <= len(contraseña):
         print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
##### ejercicio 7 ####
frase = input("Introduce una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    frase += '!'
print(frase)
##### ejercicio 8 ####
nombre = input("Introduce tu nombre: ")
opcion = int(input("Elige una opción (1: Mayúsculas, 2: Minúsculas, 3: Primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida.")
##### ejercicio 9 ####  
magnitud = float(input("Introduce la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala)." )
