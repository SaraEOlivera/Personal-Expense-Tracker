# design a text menu (e.g., "1. Add item, 2. View items, 3. Exit") 
# using a while loop and match/if statements.

def imprimir():

    print("Bienvenido al menu")
    print("Opción 1 para agregar gasto")
    print("Opción 2 para ver los gastos ingresados")
    print("Opción 3 para salir del programa")

def main():
    imprimir()
    while True:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            print("Acá se podrá agregar nuevos gastos")
        elif opcion == 2:
            print("Acá se podrán ver los gastos")
        elif opcion == 3:
            print("Fin del programa")
            break
        else:
            print("Error. Ingrese una opción correcta.")

if __name__ == "__main__":
    main()
