# design a text menu (e.g., "1. Add item, 2. View items, 3. Exit") 
# using a while loop and match/if statements.
lista_gastos = []

def imprimir():

    print("Bienvenido al menu")
    print("Opción 1 para agregar gasto")
    print("Opción 2 para ver los gastos ingresados")
    print("Opción 3 para salir del programa")

def agregar_gasto():
    gasto = float(input("Ingrese el importe del gasto: "))
    lista_gastos.append(gasto)
    print("Importe ingresado correctamente.")

def main():
    imprimir()
    while True:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_gasto()
        elif opcion == 2:
            print("Acá se podrán ver los gastos")
        elif opcion == 3:
            print("Fin del programa")
            break
        else:
            print("Error. Ingrese una opción correcta.")

if __name__ == "__main__":
    main()
