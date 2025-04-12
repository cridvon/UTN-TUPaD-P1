# Práctico 4: Estructuras repetitivas
# Objetivo:
# Implementar ciclos para resolver problemas que requieran repetición de
# acciones.

# Resultados de aprendizaje:
# 1. Diseño y Desarrollo de Algoritmos Eficientes: El estudiante será capaz de diseñar y
# desarrollar algoritmos utilizando estructuras de control repetitivas (FOR, WHILE) para
# resolver problemas matemáticos y de lógica, aplicando
# correctamente operaciones matemáticas y cálculos.
# 2. Escritura Eficaz de Pseudocódigo y Documentación: El estudiante podrá escribir
# pseudocódigo de manera estructurada y clara, utilizando comentarios para explicar el
# funcionamiento de cada parte del algoritmo.
# 3. Interacción con el Usuario y Validación de Datos: El estudiante será capaz de
# diseñar programas que interactúen con el usuario, solicitando datos de entrada y
# proporcionando resultados claros y concisos.


# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)    


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un numero: ")) 

print(f"El numero {num} tiene {len(str(num))} digitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.


num1, num2 = 0, 0
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0


for i in range(num1 + 1, num2): 
    suma += i

print(f"La suma de los numeros entre {num1} y {num2} es: {suma}")





# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.


num = int(input("Ingrese un numero: "))
suma = 0    

while num != 0:
    suma += num
    num = int(input("Ingrese un numero: "))     

print(f"La suma de los numeros ingresados es: {suma}")  


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num = random.randint(0, 9)
intentos = 0

intentos += 1
num_ingresado = int(input("Ingrese un numero: "))

while num_ingresado != num:
    intentos += 1
    num_ingresado = int(input("Ingrese un numero: "))
    if num_ingresado > num:
        print("El numero ingresado es mayor al numero a adivinar")
    else:
        print("El numero ingresado es menor al numero a adivinar")

print(f"El numero a adivinar era {num} y lo adivinaste en {intentos} intentos")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)




# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = 0
suma = 0

while num <= 0:
    num = int(input("Ingrese un numero entero positivo: "))


for i in range(num + 1):
    suma += i

print(f"La suma de los numeros entre 0 y {num} es: {suma}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

rango = 100 # Cambiar a 100 para el ejercicio final
num = 0 

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(rango):
    num = int(input("Ingrese un numero: "))

    if num % 2 == 0: # El numero es par
        pares += 1 # Incrementa la cantidad de pares
    else:
        impares += 1 # Incrementa la cantidad de impares

    if num > 0: # El numero es positivo
        positivos += 1 # Incrementa la cantidad de positivos
    elif num < 0:
        negativos += 1 # Incrementa la cantidad de negativos
    # Si el numero es 0 no se incrementa nada

print(f"Hay {pares} numeros pares, {impares} numeros impares, {positivos} numeros positivos y {negativos} numeros negativos")




# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).


rango = 100 # Cambiar a 100 para el ejercicio final
num = 0

suma = 0

for i in range(rango):
    num = int(input("Ingrese un numero: "))
    suma += num

media = suma / rango # calculo de la media

print(f"La media de los numeros ingresados es: {media}")




# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

# Pedimos al usuario un número entero
numero = int(input("Ingresa un número: "))

# Variable para guardar el número invertido
numero_invertido = 0

# Bucle para invertir el número
while numero > 0:
    digito = numero % 10              # Extraemos el último dígito del número para invertirlo

    numero_invertido = numero_invertido * 10 + digito  # Lo agregamos al número invertido

    numero = numero // 10             # Eliminamos el último dígito del número original


# Mostramos el número invertido
print("Número invertido:", numero_invertido)
