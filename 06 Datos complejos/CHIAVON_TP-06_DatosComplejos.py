# Actividades 
# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700    
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.

lista_frutas = list(precios_frutas.keys())
print("Las frutas sin precios son:", lista_frutas)  



# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
#     Contactos = {'Juan': '123456', 'Ana': '987654'} 
#     #consultar: "juan" --> muestra "El número de Juan es 123456"

def cargar_contactos():
    contactos = {}
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        numero = input("Ingrese el número de teléfono: ")
        contactos[nombre] = numero
    return contactos    

def consultar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a consultar: ")
    numero = contactos.get(nombre)
    if numero:
        print(f"El número de {nombre} es {numero}")
    else:
        print(f"No se encontró el contacto {nombre}")    
    return contactos    

# Cargar contactos
contactos = cargar_contactos()

# Consultar contacto
contactos = consultar_contacto(contactos)   



# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# Ejemplo:

# #Entrada: "hola mundo hola"
# # Salida:
# # Palabras únicas: {'hola', 'mundo'}
# # Recuento: {'hola': 2, 'mundo': 1}

frase = input("Ingrese una frase: ")
palabras = set(frase.split())
recuento = {}

for palabra in palabras:
    recuento[palabra] = frase.count(palabra)

print("Palabras únicas:", palabras)
print("Recuento:", recuento)



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:

# alumnos = {
#     'Sofía': (10, 9, 8),
#     'Luis': (6, 7, 7),
# }

alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
    notas2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
    notas3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
    notas = (notas1, notas2, notas3)
    alumnos[nombre] = notas



for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")
    

# 7) Dado dos sets de números, representando dos listas de nombres de estudiantes que aprobaron Parcial 1 
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Ana", "Luis", "Pedro", "Sofía"}
parcial2 = {"Luis", "Sofía", "María", "Juan"}

aprobados_ambos = parcial1.intersection(parcial2)
aprobados_uno = parcial1.symmetric_difference(parcial2)
aprobados_total = parcial1.union(parcial2)

print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_uno)
print("Lista total de estudiantes que aprobaron al menos un parcial:", aprobados_total)




# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

inventario = {
    "Manzanas": 50,
    "Bananas": 30,
    "Naranjas": 20    
}

opcion = 0

while opcion != 4: 
    print("1. Consultar stock")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = int(input("Ingrese una opión: "))

    if opcion == 1:
        for producto, stock in inventario.items():
            print(f"El stock de {producto} es: {stock} unidades")
    elif opcion == 2:    
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese las unidades a agregar: "))
        if producto in inventario:
            inventario[producto] += unidades
        else:
            print(f"No se encuentra el producto {producto}. Agregue un nuevo producto.")
    elif opcion == 3:
        producto = input("Ingrese el nombre del producto: ")    
        unidades = int(input("Ingrese las unidades a agregar: "))
        inventario[producto] = unidades
    elif opcion == 4:
        print("Saliendo del programa...")
        





# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:

# agenda = {
#     ("lunes", 10:00"): "Reunión con el equipo",
#     ("martes", 15:00): "Clase de ingles"
# }

# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Reunión con el equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Desayuno con cliente"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
evento = agenda.get((dia, hora))

if evento:
    print(f"En {dia} a las {hora} hay: {evento}")
else:   
    print(f"No hay eventos programados para {dia} a las {hora}.")   

    



# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:

# original = {
#     "Argentina": "Buenos Aires",
#     "Uruguay": "Montevideo",
#     "Chile": "Santiago"
# }

# invertido = {
#     "Buenos Aires": "Argentina",    
#     "Montevideo": "Uruguay",
#     "Santiago": "Chile"
# }

original = {
    "Argentina": "Buenos Aires",
    "Uruguay": "Montevideo",
    "Chile": "Santiago"
}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais
    
print("Diccionario original:", original)
print("-" * 50)
print("Diccionario invertido:", invertido)


