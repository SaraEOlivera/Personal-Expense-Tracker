import funciones

def main():
    salir = False
    try:
        while salir == False:
            try:
                lista_gastos = []
                funciones.leer_archivo(lista_gastos)
                funciones.ver_gastos(lista_gastos)
                print("*********************")
                print("Bienvenido al menu")
                print("1. Agregar gasto")
                print("2. Modificar un gasto")
                print("3. Eliminar un gasto")
                print("0. Salir")

                opcion = int(input("Ingrese una opcion del menú: "))
                match opcion:
                    case 1: funciones.agregar_gasto()
                    case 2: funciones.actualizar_gastos(lista_gastos)
                    case 3: funciones.eliminar_gastos(lista_gastos)
                    case 0: salir = True
                    case _: salir = True
            except ValueError:
                print("Elegir una opción del menú.")
            except Exception as e:
                print(f"{e}. Error.")
            # subprocess.run(["cls"], shell=True)
    except KeyboardInterrupt:
        print("Interrupió las opciones")
    finally:
        print("Fin del programa")

if __name__ == "__main__":
    main()
