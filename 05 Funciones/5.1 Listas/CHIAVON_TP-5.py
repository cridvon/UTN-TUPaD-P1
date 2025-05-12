# Práctico 5: Listas
# Objetivo:
# Desarrollar la comprensión y la capacidad de manipular listas en Python
# mediante la aplicación de conceptos fundamentales como la indexación, la
# modificación de elementos, el uso de métodos integrados y el manejo de
# listas anidadas.
# Resultados de aprendizaje:
# 1. Reconocer y aplicar correctamente la indexación y el slicing para acceder a elementos
# individuales o subconjuntos dentro de una lista.
# 2. Utilizar los métodos básicos de listas para crear, modificar y gestionar estructuras de
# datos simples.
# 3. Modificar listas mediante la actualización de valores y el manejo de listas anidadas,
# comprendiendo cómo acceder a datos en estructuras más complejas.



# Actividades

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_multiplos_4 = []

for i in range(4, 101, 4):
    lista_multiplos_4.append(i)

print("Lista de múltiplos de 4 del 1 al 100:")
print(lista_multiplos_4)    




# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista = ["perro", "gato", "conejo", "pez", "loro"]
print("El penúltimo elemento de la lista es:", lista[-2])   


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

lista_vacia = []
lista_vacia.append("perro")
lista_vacia.append("gato")
lista_vacia.append("conejo")
print("La lista resultante es:", lista_vacia)


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
print("La lista original es:", animales)

animales[1] = "loro"
animales[-1] = "oso"
print("La lista resultante es:", animales)  




# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)

# RESPUESTA:
# El programa crea una lista llamada "numeros" que contiene cinco números enteros. Luego, utiliza la función
# max() para encontrar el valor máximo en la lista y lo elimina utilizando el método remove(). Finalmente, imprime
# la lista resultante por pantalla.

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.


lista_numeros = []
for i in range(10, 31, 5):
    lista_numeros.append(i)

print("Los dos primeros números de la lista son:", lista_numeros[:2])   


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
print("La lista original es:", autos)

autos[1:3] = ["UP!", "T-Cross"]  # Alternativa para reemplazar ambos valores a la vez
print("La lista resultante es:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("La lista resultante es:", dobles)


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print("La lista original es:", compras)

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("La lista resultante es:", compras)       


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantall  

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("La lista resultante es:", lista_anidada) 