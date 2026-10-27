# design a text menu (e.g., "1. Add item, 2. View items, 3. Exit") 
# using a while loop and match/if statements.
lista_gastos = []

def imprimir():

    print("Bienvenido al menu")
    print("Opción 1 para agregar gasto")
    print("Opción 2 para ver los gastos ingresados")
    print("Opción 3 para eliminar uno de los gastos ingresados")
    print("Opción 4 para modificar uno de los gastos ingresados")
    print("Opción 5 para salir del programa")

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
    gasto = int(input("Ingrese el num de gasto que quiere modificar: "))
    modificado = float(input("Ingrese el nuevo importe: "))
    lista_gastos[gasto-1] = modificado

def eliminar_gastos():
    while True:
        try:
            gasto = int(input("Ingrese el num de gasto que quiere eliminar: "))
            if gasto <= 0 or gasto > len(lista_gastos):
                print("Ingreso un numero de gasto incorrecto.")
                break
            else:
                lista_gastos.pop(gasto-1)
                break
        except Exception as e:
            print("Error. No se ingresó un número")


def main():
    imprimir()
    while True:
        try:
            opcion = int(input("Ingrese una opcion del menú: "))
            if opcion == 1:
                agregar_gasto()
            elif opcion == 2:
                print("Estos son los gastos ingresados: ")
                ver_gastos()
            elif opcion == 3:
                eliminar_gastos()
                # print("Gasto Eliminado:")
                ver_gastos()
            elif opcion == 4:
                actualizar_gastos()
                print("Gasto Modificado:")
                ver_gastos()
            elif opcion == 5:
                print("Fin del programa")
                break
            else:
                print("Error. Ingrese una opción correcta.")
        except ValueError:
            print("Opción incorrecta. Ingrese una opción del menú.")


if __name__ == "__main__":
    main()
