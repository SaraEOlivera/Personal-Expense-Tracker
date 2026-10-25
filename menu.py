# design a text menu (e.g., "1. Add item, 2. View items, 3. Exit") 
# using a while loop and match/if statements.
lista_gastos = []

def imprimir():

    print("Bienvenido al menu")
    print("Opción 1 para agregar gasto")
    print("Opción 2 para ver los gastos ingresados")
    print("Opción 3 para eliminar uno de los gastos ingresados")
    print("Opción 4 para salir del programa")

def agregar_gasto():
    gasto = float(input("Ingrese el importe del gasto: "))
    lista_gastos.append(gasto)
    print("Importe ingresado correctamente.")

def ver_gastos():
    gasto = 0
    for i in range(len(lista_gastos)):
        gasto += 1
        print(f"Gasto {gasto}: {lista_gastos[i]}")


def actualizar_gastos():
    pass

def eliminar_gastos():
    gasto = int(input("Ingrese el num de gasto que quiere eliminar: "))
    lista_gastos.pop(gasto-1)

def main():
    imprimir()
    while True:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_gasto()
        elif opcion == 2:
            print("Estos son los gastos ingresados: ")
            ver_gastos()
        elif opcion == 3:
            eliminar_gastos()
            print("Gasto Eliminado")
        elif opcion == 4:
            print("Fin del programa")
            break
        else:
            print("Error. Ingrese una opción correcta.")

if __name__ == "__main__":
    main()
