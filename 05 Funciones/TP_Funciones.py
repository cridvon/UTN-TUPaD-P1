# Actividades:
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

""" def imprimir_hola_mundo():
    print("Hola Mundo!")    

# Llamada a la función
imprimir_hola_mundo()
 """
    


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de￾volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

""" # Definición de la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Ejecución del programa principal
nombre_usuario = input("Ingrese su nombre: ")   
print(saludar_usuario(nombre_usuario))
 """



# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe￾dir los datos al usuario y llamar a esta función con los valores in￾gresados.

""" # Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejecución del programa principal
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario) """


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra￾dio como parámetro y devuelva el área del círculo.
# calcular_peri￾metro_circulo(radio) que reciba el radio como parámetro y devuel￾va el perímetro del círculo. 
# Solicitar el radio al usuario y llamar am￾bas funciones para mostrar los resultados.

""" import math

# Definición de las funciones
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)       

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejecución del programa principal
radio_usuario = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

 """


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos￾trar el resultado usando esta función.

""" # Definición de la función
def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos"

# Ejecución del programa principal
segundos_usuario = int(input("Ingrese la cantidad de segundos: "))
resultado = segundos_a_horas(segundos_usuario)

print(f"El tiempo equivalente es: {resultado}")

 """

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun￾ción.

""" # Definición de la función
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejecución del programa principal

numero_usuario = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)       

 """

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta￾do de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los re￾sultados de forma clara.

""" # Definición de la función
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)

# Ejecución del programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Resultados:\nSuma: {resultados[0]}\nResta: {resultados[1]}\nMultiplicación: {resultados[2]}\nDivisión: {resultados[3]}")

 """

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun￾ción para mostrar el resultado con dos decimales.

""" # Definición de la función
def calcular_imc(peso, altura):
    if altura <= 0:
        return "Error: La altura debe ser mayor que cero."
    imc = peso / (altura ** 2)
    return f"El IMC es: {imc:.2f}"

# Ejecución del programa principal
peso_usuario = float(input("Ingrese su peso en kg: "))
altura_usuario = float(input("Ingrese su altura en metros: "))
resultado_imc = calcular_imc(peso_usuario, altura_usuario)
print(resultado_imc)
 """


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

""" # Definición de la función
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C es equivalente a {fahrenheit:.2f}°F"   

# Ejecución del programa principal
celsius_usuario = float(input("Ingrese la temperatura en grados Celsius: "))
resultado_fahrenheit = celsius_a_fahrenheit(celsius_usuario)
print(resultado_fahrenheit)
 """


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Definición de la función
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return f"El promedio de {a}, {b} y {c} es: {promedio:.2f}"

# Ejecución del programa principal
a_usuario = float(input("Ingrese el primer número: "))
b_usuario = float(input("Ingrese el segundo número: "))
c_usuario = float(input("Ingrese el tercer número: "))
resultado_promedio = calcular_promedio(a_usuario, b_usuario, c_usuario)
print(resultado_promedio)

