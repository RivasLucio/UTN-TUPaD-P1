
#  2
mis_elementos = ["pizza", "chocolate", "helado", "pasta", "sushi"]
print( mis_elementos[-2])

#  3
lista_vacia = []
lista_vacia.append("palabra1")
lista_vacia.append("palabra2")
lista_vacia.append("palabra3")
print(lista_vacia)

#  4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#  5
#elimina unicamente el valor mas alto, quedando 8, 15, 3, 7

#  6
numeros = list(range(10, 31, 5))
print(numeros[:2])

#  7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print(autos)

#  8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#  9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")  # a)
compras[1][1] = "tallarines"  # b)
compras[0].remove("pan")  # c)
print(compras)

#  10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)