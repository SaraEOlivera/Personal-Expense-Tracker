# design a text menu (e.g., "1. Add item, 2. View items, 3. Exit") 
# using a while loop and match/if statements.
lista_gastos = {}


def imprimir():

    print("Bienvenido al menu")
    print("Opción 1 para agregar gasto")
    print("Opción 2 para ver los gastos ingresados")
    print("Opción 3 para eliminar uno de los gastos ingresados")
    print("Opción 4 para modificar uno de los gastos ingresados")
    print("Opción 5 para salir del programa")

def agregar_gasto():
    try:
        detalle = input("Ingrese el detalle del gasto: ")
        gasto = float(input("Ingrese el importe del gasto: "))
        if gasto <= 0:
            raise ValueError("El importe de gasto no puede ser 0 o un numero negativo")
        lista_gastos[detalle] = gasto
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
        for x, y in lista_gastos.items():
            print(f"{x}: {y}")

def actualizar_gastos():
    try:
        if len(lista_gastos) == 0:
            print("No hay datos para modificar")
            return
        else:
            respuesta = int(input("Ingresa 1 para modificar detalle 2 para modificar gasto "))
            if respuesta == 1:
                detalle = input("Que gasto queres modificar? ")
                if detalle in lista_gastos:
                    nuevo_detalle = input("Cual es el nuevo detalle? ")
                    lista_gastos[nuevo_detalle] = lista_gastos.pop(detalle)
                    print("Detalle modificado")
            # gasto = int(input("Ingrese el num de gasto que quiere modificar: "))
            # if gasto <= 0:
            #     raise ValueError("El num de gasto no puede ser 0 o un numero negativo")
            # modificado = float(input("Ingrese el nuevo importe: "))
            # if modificado <= 0:
            #     raise ValueError("El gasto no puede ser inferior a 0.")
            # lista_gastos[gasto-1] = modificado
    except ValueError:
        print("Ingresar datos de forma numérica y mayores a 0")

def eliminar_gastos():
    while True:
        try:
            if len(lista_gastos) == 0:
                print("No hay gastos para eliminar")
                break
            else:
                detalle = input("Qué gasto quiere eliminar: ")
                if detalle in lista_gastos:
                    lista_gastos.pop(detalle)
                    print("Gasto eliminado ok")
                    break
                # gasto = int(input("Ingrese el num de gasto que quiere eliminar: "))
                # if gasto <= 0 or gasto > len(lista_gastos):
                #     print("Ingreso un numero de gasto incorrecto.")
                #     break
                else:
                    # lista_gastos.pop(gasto-1)
                    print("Ese gasto no está en tu lista")
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
