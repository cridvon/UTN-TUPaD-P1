#Creación, visualización y recorridos de un ARBOL utilizando LISTAS con
#inserción y búsqueda de nodos.

#Importamos libreria para limpiar la pantalla
import os

# -------------------------- FUNCIONES --------------------------
#Crea el arbol con el nodo Raiz
def crear_arbol(arbol):
    #Verifica que el arbol NO exista
    if not arbol:
        arbol = [int(input("Ingrese el nodo raiz del árbol: ")),[],[]]
        return arbol
    else:
        return False  


# "Dibuja" el árbol para visualizarlo
def dibujar_arbol(arbol, nivel=0, prefijo="Raíz: "):
    sangria = "    " * nivel
    print(f"{sangria}{prefijo}{arbol[0]}")
    
    # Recorremos los subárboles
    if arbol[1]:
        dibujar_arbol(arbol[1], nivel + 1, "Izq: ")
    if arbol[2]:
        dibujar_arbol(arbol[2], nivel + 1, "Der: ")
    return
        

#Agrega un nodo hijo al arbol
def agregar_nodo(arbol, nodo):
    #Verifica que el arbol exista
    if arbol[0]:
        if arbol[0] == nodo:
            print("Este valor ya se encuentra en el árbol")
            return
        if nodo < arbol[0]:
            if arbol[1]:
                agregar_nodo(arbol[1], nodo)
            else:
                arbol[1]=[nodo,[],[]]
                print("Valor agregado al árbol")
        if nodo > arbol[0]:
            if arbol[2]:
                agregar_nodo(arbol[2],nodo)
            else:
                arbol[2]=[nodo,[],[]]
                print("Valor agregado al árbol")
    else:
        arbol[0]=[nodo,[],[]]
        print("Valor agregado al árbol")
    return



#Verifica si el valor ingresado existe en el arbol
def buscar_nodo(arbol,nodo):
    #Verifica que el arbol exista
    if arbol[0]:
        if arbol[0] == nodo:
            print(f"El valor {nodo} se encuetra en el árbol")
            return
        if nodo < arbol[0]:
            if arbol[1]:
                buscar_nodo(arbol[1], nodo)
            else:
                print(f"El valor {nodo} NO se encuentra en el árbol")
        if nodo > arbol[0]:
            if arbol[2]:
                buscar_nodo(arbol[2],nodo)
            else:
                print(f"El valor {nodo} NO se encuentra en el árbol")
    else:
        print(f"El valor {nodo} NO se encuentra en el árbol")
    return


#LLama a los diferentes métodos para recorrer el árbol
def recorrer_arbol(arbol):
    print("--- Recorrido InOrder ---")
    recorrer_arbol_inOrder(arbol)
    print("\n")
    print("--- Recorrido PreOrder ---")
    recorrer_arbol_preOrder(arbol)
    print("\n")
    print("--- Recorrido PostOrder ---")
    recorrer_arbol_postOrder(arbol)
    print("\n")


#Recorre el arbol INORDER (hoja izq, Nodo, Hoja derecha)
def recorrer_arbol_inOrder(arbol):
    if arbol[1]:
        recorrer_arbol_inOrder(arbol[1])
    print(arbol[0],end=" - ") 
    if arbol[2]:
        recorrer_arbol_inOrder(arbol[2])
    return


#Recorre el arbol PREORDER (Nodo, hoja izq, Hoja derecha)
def recorrer_arbol_preOrder(arbol):
    print(arbol[0], end=" - ")
    if arbol[1]:
        recorrer_arbol_preOrder(arbol[1])
    if arbol[2]:
        recorrer_arbol_preOrder(arbol[2])
    return

#Recorre el arbol POSTORDER (hoja izq, Hoja derecha, Nodo)
def recorrer_arbol_postOrder(arbol):
    if arbol[1]:
        recorrer_arbol_postOrder(arbol[1])
    if arbol[2]:
        recorrer_arbol_postOrder(arbol[2])
    print(arbol[0], end=" - ")
    return
# -------------------------- FIN FUNCIONES --------------------------


# -------------------------- INICIO DEL PROGRAMA --------------------------

#Arbol Lista con valores pre-definidos
# arbol=[50,[30,[20,[10,[],[12,[],[]]],[]],[40,[],[]]],[70,[60,[],[65,[],[]]],[80,[],[]]]]

arbol=[]
salir=-1
while salir != 0:
    os.system('cls')
    print("-"*30)
    print("Seleccione una opción: ")
    print("-"*30)
    print("1 - Crear árbol")
    print("2 - Visualizar árbol")
    print("3 - Agregar Nodo")
    print("4 - Buscar valor en árbol")
    print("5 - Recorrer árbol ( InOrder / PreOrder / PostOrder )")
    print("0 - Salir")
    print("-"*30)
    opcion=int(input("Opcion: "))
    print("-"*30)
    match opcion:
        case 1:
            os.system('cls')
            #Retorna el arbol creado o "False" si ya existe
            raiz =  crear_arbol(arbol)
            if raiz == False:
                print("El árbol ya existe")
            else:
                arbol=raiz
                print("Árbol creado")
            input("Presione enter para volver...")     
        case 2:
            os.system('cls')
            #Verifica que el arbol exista
            if arbol:
                dibujar_arbol(arbol)
            else:
                print("El árbol aun no existe. Favor de crearlo..")
            input("Presione enter para volver...")
        case 3:
            os.system('cls')
            if arbol:
                nodo = int(input("Ingrese el valor a agregar: "))
                agregar_nodo(arbol, nodo)
            else:
                print("El árbol aun no existe. Favor de crearlo..")
            input("Presione enter para volver...")
        case 4:
            os.system('cls')
            if arbol:
                nodo = int(input("Ingrese el valor a buscar: "))
                buscar_nodo(arbol,nodo)
            else:
                print("El árbol aun no existe. Favor de crearlo..")
            input("Presione enter para volver...")
        case 5:
            os.system('cls')
            if arbol:
                recorrer_arbol(arbol)
            else:
                print("El árbol aun no existe. Favor de crearlo..")
            input("Presione enter para volver...")
        case 0:
            print("Saliendo del sistema....")
            salir=0
        case _:
            os.system('cls')
            print("Esa opcion no es válida")
            input("Presione enter para volver...")

# -------------------------- FIN PROGRAMA --------------------------