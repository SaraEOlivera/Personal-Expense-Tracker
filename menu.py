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
    try:
        gasto = float(input("Ingrese el importe del gasto: "))
        if gasto <= 0:
            raise ValueError("El importe de gasto no puede ser 0 o un numero negativo")
        lista_gastos.append(gasto)
        print("Importe ingresado correctamente.")
    except ValueError:
        print("Excribir los gastos de forma numérica y mayores a 0.")
    except Exception as e:
        print(f"{e}. Error.")

def ver_gastos():
    gasto = 0
    if len(lista_gastos) == 0:
        print("No hay gastos registrados")
    else:
        for i in range(len(lista_gastos)):
            gasto += 1
            print(f"Gasto {gasto}: {lista_gastos[i]}")


def actualizar_gastos():
    if len(lista_gastos) == 0:
        print("No hay gastos registrados")
    try:
        gasto = int(input("Ingrese el num de gasto que quiere modificar: "))
        if gasto <= 0:
            raise ValueError("El num de gasto no puede ser 0 o un numero negativo")
        modificado = float(input("Ingrese el nuevo importe: "))
        if modificado <= 0:
            raise ValueError("El gasto no puede ser inferior a 0.")
        lista_gastos[gasto-1] = modificado
    except ValueError:
        print("Ingresar datos de forma numérica y mayores a 0")

def eliminar_gastos():
    if len(lista_gastos) == 0:
        print("No hay gastos registrados")
    while True:
        try:
            gasto = int(input("Ingrese el num de gasto que quiere eliminar: "))
            if gasto <= 0 or gasto > len(lista_gastos):
                print("Ingreso un numero de gasto incorrecto.")
                break
            else:
                lista_gastos.pop(gasto-1)
                break
        except ValueError:
            print("No ingreso un numero de gasto")
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
                # print("Gasto Modificado:")
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
