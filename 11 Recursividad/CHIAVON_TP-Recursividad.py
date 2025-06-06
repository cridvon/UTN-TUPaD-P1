# Ejercicios
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario


def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:    
        return 1
    else:
        # Llamada recursiva: n * factorial de (n - 1)
        return n * factorial(n - 1)  

# Función para mostrar los factoriales desde 1 hasta n
def mostrar_factoriales_hasta(n):
    # Recorre todos los números del 1 al n
    for i in range(1, n + 1):
        # Muestra el factorial de cada número i
        print(f"El factorial de {i} es: {factorial(i)}")

# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Mostrar los factoriales desde 1 hasta el número ingresado
mostrar_factoriales_hasta(n)



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Función recursiva para calcular el n-ésimo término de la serie de Fibonacci
def fibonacci(n):
    # Caso base: el término 0 es 0
    if n <= 0:
        return 0
    # Caso base: el término 1 es 1
    elif n == 1:
        return 1
    else:
        # Llamada recursiva: suma de los dos términos anteriores
        return fibonacci(n - 1) + fibonacci(n - 2)

# Función para mostrar todos los elementos de la serie de Fibonacci hasta n
def mostrar_serie_fibonacci_hasta(n):
    # Recorre desde 0 hasta n (inclusive)
    for i in range(n + 1):
        # Muestra el i-ésimo elemento de la serie
        print(f"El elemento {i} de la serie de Fibonacci es: {fibonacci(i)}")

# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))   


#mostrar el valor de la serie de Fibonacci en la posición indicada
print(f"El valor de la serie de Fibonacci en la posición {n} es: {fibonacci(n)}")

# Mostrar la serie de Fibonacci desde 0 hasta el número ingresado
mostrar_serie_fibonacci_hasta(n)




# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 a la m = 𝑛 ∗ 𝑛 a la (𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else:
        # Multiplicar la base por sí misma (exponente - 1) veces
        return base * potencia(base, exponente - 1)
    
# Solicitar al usuario la base y el exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calcular la potencia y mostrar el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este procedimiento:
#     1. Dividir el número por 2.
#     2. Guardar el resto (0 o 1).
#     3. Repetir el proceso con el cociente hasta que llegue a 0.
#     4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

#     🧠Ejemplo:
#     Convertir el número 10 a binario:
#     10 ÷ 2 = 5 resto: 0 
#     5 ÷ 2 = 2 resto: 1 
#     2 ÷ 2 = 1 resto: 0 
#     1 ÷ 2 = 0 resto: 1 
#     Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def decimal_a_binario(n):
    # Caso base: cuando n es 0, devuelve una cadena vacía (termina la recursión)
    if n == 0:
        return ""
    else:
        # Llamada recursiva: divide n entre 2 (parte entera)
        # Luego concatena el resto (n % 2) convertido a cadena
        return decimal_a_binario(n // 2) + str(n % 2)

    
# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Convertir el número a binario y mostrar el resultado
binario = decimal_a_binario(n)
print(f"El número {n} en binario es: {binario}")    




# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().



def es_palindromo(palabra):
    # Creamos una nueva cadena vacía para guardar la palabra recortada
    nueva_palabra = ""
    
    # Índice del primer caracter
    primera = 0
    # Índice del último caracter
    ultima = len(palabra) - 1

    # Caso base: si la palabra tiene 0 o 1 letras, es un palíndromo
    if len(palabra) <= 1:
        return True
    else:
        # Comparamos el primer y último carácter
        if palabra[primera] == palabra[ultima]:
            # Si son iguales, construimos una nueva palabra sin los extremos
            for i in range(1, len(palabra) - 1):
                nueva_palabra += palabra[i]
            # Llamamos recursivamente con la palabra recortada
            return es_palindromo(nueva_palabra)
        else:
            # Si los caracteres no son iguales, no es palíndromo
            return False


# Solicitar al usuario una palabra
palabra = input("Ingrese una palabra sin espacios ni tildes: ")
# Verificar si la palabra es un palíndromo
print(es_palindromo(palabra)) 


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)


def suma_digitos(n):
    # Caso base: si n es 0, la suma de los dígitos es 0
    if n == 0:
        return 0
    else:
        # Sumar el último dígito (n % 10) y llamar recursivamente con el resto del número (n // 10)
        return (n % 10) + suma_digitos(n // 10) 

# Solicitar al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))
# Calcular la suma de los dígitos
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    # Caso base: si n es 1, no hay mas bloques despues
    if n == 1:
        return 1
    else:
        # Sumar el número de bloques en el nivel actual (n) y llamar recursivamente con el nivel anterior (n - 1)
        return n + contar_bloques(n - 1)
    
# Solicitar al usuario el número de bloques en el nivel más bajo
n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
# Calcular el total de bloques  
print(f"El total de bloques para construir la pirámide es: {contar_bloques(n)}")


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3 
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0  """

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos para contar
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito del número es igual al dígito buscado
        if numero % 10 == digito:
            # Sumar 1 y llamar recursivamente con el resto del número (número // 10)
            return 1 + contar_digito(numero // 10, digito)
        else:
            # Llamar recursivamente sin sumar, solo con el resto del número
            return contar_digito(numero // 10, digito)
        
# Solicitar al usuario el número y el dígito a contar
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar: "))
# Calcular la cantidad de veces que aparece el dígito
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}")