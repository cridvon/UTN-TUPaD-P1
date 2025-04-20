# Trabajo Integrador de Matematica | TUPaD | Comisión 11 | Grupo 5

# Campana Mario
# Chiavón Cristian
# Chiavón Facundo
# Choque Javier

#region IMPORTACIONES ----------------------
from math import trunc # Importa la función trunc de la librería math para truncar números decimales
import random # Importa la librería random para generar números aleatorios
import os # Importa la librería os para limpiar la pantalla
from colorama import init, Fore, Style  # 'init' inicializa colorama. 'Fore' y 'Style' son para aplicar colores.
#endregion

init()  # Inicializa colorama

# FUNCIONES ------------------------

#region Función para convertir un número decimal a su representación binaria
def binario(n):
    binFinal = ""  # Variable para almacenar el resultado final en formato binario
    binArray = []  # Lista para almacenar los dígitos binarios
    if n == 0:
        binArray[0] = 0  # Manejo del caso especial cuando n es 0
    else:
        # Bucle para dividir el número por 2 y extraer el residuo
        while n != 0:
            entero = trunc(n / 2)  # Obtener la parte entera de n dividido por 2
            decimal = n % 2  # Obtener el residuo (0 o 1)
            n = entero  # Actualizar n para el siguiente ciclo
            binArray.append(decimal)  # Agregar el dígito binario a la lista
    binArray = binArray[::-1]  # Invertir la lista para obtener el orden correcto
    for i in binArray:
        binFinal = binFinal + str(i)  # Concatenar los dígitos binarios en un string
    return binFinal  # Retornar el resultado en formato binario
#endregion

#region Función para convertir un número decimal a su representación octal
def octal(n):
    octFinal = ""  # Variable para almacenar el resultado final en formato octal
    octArray = []  # Lista para almacenar los dígitos octales
    if n == 0:
        octArray[0] = 0  # Manejo del caso especial cuando n es 0
    elif n < 8:
        octFinal = str(n)  # Si n es menor que 8, es el mismo número en octal
        return octFinal
    else:
        # Bucle para dividir el número por 8 y extraer el residuo
        while n != 0:
            entero = trunc(n / 8)  # Obtener la parte entera de n dividido por 8
            decimal = n % 8  # Obtener el residuo
            n = entero  # Actualizar n para el siguiente ciclo
            octArray.append(decimal)  # Agregar el dígito octal a la lista
    octArray = octArray[::-1]  # Invertir la lista para obtener el orden correcto
    for i in octArray:
        octFinal = octFinal + str(i)  # Concatenar los dígitos octales en un string
    return octFinal  # Retornar el resultado en formato octal
#endregion

#region Función para convertir un número decimal a su representación hexadecimal
def hexa(n):
    hexLetras = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}  # Diccionario para mapeo de números a letras hexadecimales
    hexFinal = ""  # Variable para almacenar el resultado final en formato hexadecimal
    hexArray = []  # Lista para almacenar los dígitos hexadecimales
    if n == 0:
        hexArray[0] = 0  # Manejo del caso especial cuando n es 0
    elif n < 16:
        # Manejo de casos donde n es menor que 16
        if n <= 9:
            hexFinal = str(n)  # Retornar el número tal cual si es menor o igual a 9
            return hexFinal
        elif n in hexLetras:
            hexFinal = hexLetras[n]  # Retornar la letra correspondiente en caso de que n esté en el diccionario
            return hexFinal
    else:
        # Bucle para dividir el número por 16 y extraer el residuo
        while n != 0:
            entero = trunc(n / 16)  # Obtener la parte entera de n dividido por 16
            decimal = n % 16  # Obtener el residuo
            n = entero  # Actualizar n para el siguiente ciclo
            if decimal in hexLetras:
                decimal = hexLetras[decimal]  # Convertir el residuo a letra si es necesario
            hexArray.append(decimal)  # Agregar el dígito hexadecimal a la lista
    hexArray = hexArray[::-1]  # Invertir la lista para obtener el orden correcto
    for i in hexArray:
        hexFinal = hexFinal + str(i)  # Concatenar los dígitos hexadecimales en un string
    return hexFinal  # Retornar el resultado en formato hexadecimal
#endregion

#region OPCION 1: Función para CONVERTIR un número decimal a diferentes bases (binario, octal y hexadecimal)
# Esta función solicita al usuario un número decimal y lo convierte a las bases correspondientes
def conversor():
    n=-1
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú
    print(Fore.GREEN + "\n===== CONVERSION DE BASES =====" + Style.RESET_ALL)  # Título del menú
    while n<=0:
        try:
            n=int(input("\nIngrese el número decimal que desea convertir: "))
        except ValueError: # Manejo de excepción para entradas no válidas
            print(Fore.RED + "Entrada no válida. Por favor, ingrese un número natural."+ Style.RESET_ALL)
            continue
        if n<=0:
                print(Fore.RED + "El número debe ser un número positivo."+ Style.RESET_ALL)
    thickness=16
    print(("-"*65))
    # Encabezado con colores distintos
    print(
        "|" +
        Fore.YELLOW + "Decimal".center(thickness) + Style.RESET_ALL + "|" +
        Fore.CYAN + "Octal".center(thickness) + Style.RESET_ALL + "|" +
        Fore.MAGENTA + "Hexadecimal".center(thickness) + Style.RESET_ALL + "|" +
        Fore.GREEN + "Binario".center(thickness) + Style.RESET_ALL + "|"
    )

    # Separador
    print("-" * (thickness * 4 + 5))  # Ajustamos el largo total de la línea

    # Fila de valores, cada uno con su color y bien alineado
    print(
        "|" +
        Fore.YELLOW + str(n).center(thickness) + Style.RESET_ALL + "|" +
        Fore.CYAN + octal(n).center(thickness) + Style.RESET_ALL + "|" +
        Fore.MAGENTA + hexa(n).center(thickness) + Style.RESET_ALL + "|" +
        Fore.GREEN + binario(n).center(thickness) + Style.RESET_ALL + "|"
    )
    input(Fore.BLUE + "\nPresione Enter para continuar..." + Style.RESET_ALL)
#endregion

#region OPCION 2: Función para el juego de ADIVINANZA
def adivinanza():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú
    print(Fore.GREEN + "\n===== ADIVINANZA BINARIA =====" + Style.RESET_ALL)  # Título del menú
    num = random.randint(0, 100)  # Genera un número aleatorio entre 0 y 100

    # Muestra el número a adivinar en pantalla convertido a Binario usando la funcion que creeamos
    print(f"\nEl numero a adivinar en representación Binaria es: {Fore.YELLOW}{binario(num)}{Style.RESET_ALL}")

    intentos = 1  # Inicializa el contador de intentos

    # Solicita al usuario que ingrese un número
    num_ingresado = int(input("Ingrese un numero entre 0 y 100: "))

    # Bucle para verificar si el número ingresado es correcto
    while num_ingresado != num:
        if num_ingresado > num:
            print(f"El numero ingresado es {Fore.RED}mayor{Style.RESET_ALL} que numero a adivinar.")  # Indica que el número ingresadoes mayor
        else:
            print(f"El numero ingresado es {Fore.CYAN}menor{Style.RESET_ALL} que numero a adivinar.")  # Indica que el número ingresado es menor
        intentos += 1  # Incrementa el contador de intentos
        num_ingresado = int(input("Ingrese un numero: "))  # Solicita otro número al usuario


    print(f"\nEl numero a adivinar era {Fore.GREEN}{num}{Style.RESET_ALL} y lo lograste en {Fore.YELLOW}{intentos}{Style.RESET_ALL} intentos!!!")  # Muestra el resultado final

    print(f"{Fore.MAGENTA}-"*65)
    print(f"Gracias por jugar".center(65))
    print(f"-"*65)
    input(Fore.BLUE + "\nPresione Enter para continuar..." + Style.RESET_ALL)
#endregion

#region Función para limpiar la pantalla
# Esta función utiliza la librería os para limpiar la pantalla de la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpia la pantalla dependiendo del sistema operativo
#endregion

#region Función para mostrar el menú
def mostrar_menu():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú
    print(Fore.GREEN + "\n===== MENÚ PRINCIPAL =====" + Style.RESET_ALL)  # Título del menú
    print(Fore.YELLOW + "\n1." + Style.RESET_ALL + " Conversión de Bases")  # Opción 1 en amarillo
    print(Fore.YELLOW + "2." + Style.RESET_ALL + " Adivinanza Binaria")  # Opción 2 en amarillo
    print(Fore.RED + "\n0." + Style.RESET_ALL + " Salir")        # Opción de salir en rojo
#endregion

#region MAIN PROGRAM ------------------------

opcion = -1  # Inicializa la opción del menú para que no sea 0 al inicio

# Bucle principal del menú
while opcion != 0:
    # Mostrar el menú y solicitar la opción al usuario
    mostrar_menu()

    try: # Solicita al usuario que ingrese una opción
        opcion = int(input(Fore.BLUE + "\nSeleccione una opción: "+ Style.RESET_ALL))
    except ValueError: # Manejo de excepción para entradas no válidas
        print(Fore.RED + "Entrada no válida. Por favor, ingrese un número del menú."+ Style.RESET_ALL)
        input(Fore.BLUE + "\nPresione Enter para continuar..." + Style.RESET_ALL)
        continue

    if opcion == 1: # Si elige la opción 1, llama a la función conversor
        conversor()
    elif opcion == 2: # Si elige la opción 2, llama a la función adivinanza
        adivinanza()
    elif opcion == 0: # Si elige la opción 0, sale del programa
        print(Fore.MAGENTA + "Saliendo del programa. ¡Hasta luego!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Entrada no válida. Por favor, ingrese un número del menú."+ Style.RESET_ALL)
        input(Fore.BLUE + "\nPresione Enter para continuar..." + Style.RESET_ALL)
#endregion

# Mostrar funcionamiento del programa (que hace?)
# Mostrar el codigo fuente de cada funcion
    # Mostrar la parte de Importaciones
    # Mostrar la parte de Funciones
        # Mostrar la funcion binario
        # Mostrar la funcion octal
        # Mostrar la funcion hexadecimal
        # Mostrar la funcion conversor
        # Mostrar la funcion adivinanza
        # Mostrar la funcion limpiar_pantalla
        # Mostrar la funcion mostrar_menu
    # Mostrar la parte de Main Program