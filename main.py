import funciones

def main():
    salir = False
    try:
        while salir == False:
            try:
                print("*********************")
                print("Bienvenido al menú")
                print("*********************")
                print("1. Agregar gasto")
                print("2. Ver todos los gastos")
                print("3. Ver gastos por fechas")
                print("4. Modificar un gasto")
                print("5. Eliminar un gasto")
                print("6. Calcular el total de los gastos registrados")
                print("7. Calcular total de gastos de un mes")
                print("8. Agrupar gastos")
                print("0. Salir")

                opcion = int(input("Ingrese una opcion del menú: "))
                match opcion:
                    case 1: funciones.agregar_gasto(2026, 2026)
                    case 2: funciones.ver_gastos()
                    case 3: funciones.ver_un_gasto()
                    case 4: funciones.actualizar_gastos()
                    case 5: funciones.eliminar_gastos()
                    case 6: funciones.calcular_total()
                    case 7: funciones.calcular_mensual()
                    case 8: funciones.agrupar_categorias()
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
