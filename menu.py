# design a text menu (e.g., "1. Add item, 2. View items, 3. Exit") 
# using a while loop and match/if statements.
print("Bienvenido al menu")

opcion = int(input("Ingrese una opcion: 1, 2 ó 0 para salir: "))

while opcion != 0:
    match opcion:
        case 1:
            print("Ingresó la opción para agregar gasto")
            opcion = int(input("Ingrese una opcion: 1, 2 ó 0 para salir: "))
        case 2:
            print("Ingresó la opción para ver gastos")
            opcion = int(input("Ingrese una opcion: 1, 2 ó 0 para salir: "))
        # case 0:
        #     print("Ingresó la opción para salir del programa")
        #     break
        case _:
            print("Opción incorrecta.")
            opcion = int(input("Ingrese una opcion: 1, 2 ó 0 para salir: "))
if opcion == 0:
    print("salió del programa")
