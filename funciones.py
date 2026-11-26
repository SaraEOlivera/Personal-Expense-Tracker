from datetime import date
from datetime import datetime
import db

def ver_gastos():
    print("GASTOS REGISTRADOS")
    lista = db.ver_gastos()
    if not lista:
        print("No hay gastos registrados")
    else:
        print("**********************************")
        print("Estos son los gastos registrados:")
        for gasto in lista:
            detalle, importe, categoria, fecha = gasto
            print(f"{detalle}: ${importe} categoria: {categoria} - {fecha}")


def buscar_gastos():
    salir = False
    try:
        while salir == False:
            try:
                print("BUSCAR GASTOS")
                print("*********************")
                print("1. Buscar gastos por fechas")
                print("2. Buscar gastos por detalles")
                print("3. Buscar gastos por categorías")
                print("0. Volver al menú anterior")

                opcion = int(input("Ingrese una opcion para buscar gastos: "))
                if opcion == 1:
                    mes_ingresado = input("Ingrese el mes del gasto: ").strip()
                    mes_formateado = mes_ingresado.zfill(2)
                    if int(mes_formateado) < 1 or int(mes_formateado) > 12:
                        print(f"No ingresó el mes correcto: {mes_formateado}")
                        return
                    anio = input("Ingrese el año del gasto: ").strip()
                    if int(anio) < 2025 or int(anio) > 2026:
                        print(f"No ingresó el año correcto: {anio}")
                        return
                    if not mes_formateado or not anio:
                        print(f"{mes_formateado} no es un dato correcto")
                        return
                    else:
                        lista = db.buscar_gasto_mes(mes_formateado, anio)
                        if not lista:
                            print(f"No hay gastos registrados el mes {mes_formateado} de {anio}")
                        else:
                            print("**********************************")
                            print(f"Gastos registrados el {mes_formateado} de {anio}:")
                            for gasto in lista:
                                detalle, importe, fecha = gasto
                                print(f"{detalle}: ${importe} - {fecha}")


                elif opcion == 2:
                    detalle = input("Ingrese el detalle de los gastos que busca: ").strip()
                    lista = db.buscar_gasto_detalle(detalle)
                    if not lista:
                        print(f"No hay gastos registrados con el detalle {detalle}")
                    else:
                        print("**********************************")
                        print(f"Estos son los gastos registrados con detalle {detalle}:")
                        for gasto in lista:
                            detalle, importe, fecha = gasto
                            print(f"{detalle}: ${importe} - {fecha}")

                elif opcion == 3:
                    categoria = input("Ingrese la categoria de los gastos que busca: ").strip()
                    lista = db.buscar_gasto_categoria(categoria)
                    if not lista:
                        print(f"No hay gastos registrados bajo la categoría {categoria}")
                    else:
                        print("**********************************")
                        print(f"Estos son los gastos registrados con categoría {categoria}:")
                        for gasto in lista:
                            detalle, importe, fecha = gasto
                            print(f"{detalle}: ${importe} - {fecha}")

                elif opcion == 0:
                    salir = True
                else:
                    salir = True
            except ValueError:
                print("Elegir una opción para buscar gastos.")
            except Exception as e:
                print(f"{e}. Error.")
    except KeyboardInterrupt:
        print("Interrupió las opciones")
    finally:
        print("Vuelve al menu anterior")

def agregar_gasto(anio_min:int, anio_max:int)-> str:
    print("AGREGAR UN GASTO:")
    try:
        detalle = input("Ingrese el detalle del gasto: ").strip()
        categoria = input("Ingrese categoria del gasto: ").strip()
        if not detalle or not categoria:
            print(f"Ingresó campo vacío")
            return
        elif not detalle.isalpha() or not categoria.isalpha():
            print("No ingresar caracteres especiales")
            return
        elif detalle.isnumeric() or categoria.isnumeric():
            print("Debe ingresar texto")
            return
        importe = float(input("Ingrese el importe del gasto: "))
        if importe <= 0:
            print("El importe de gasto no puede ser 0 o un numero negativo")
            return
        fecha = input(f"Ingrese la fecha del gasto (DD-MM-YYYY) entre {anio_min} y {anio_max}: ").strip()
        try:
            fecha_ingresada = datetime.strptime(fecha, "%d-%m-%Y")
            if not (anio_min <= fecha_ingresada.year <= anio_max):
                print(f"El año debe ser entre {anio_min} y {anio_max}")
                return
            fecha_modificada = fecha_ingresada.strftime("%Y-%m-%d")
        except ValueError:
            print("Ingrese fecha con formato DD-MM-YYYY")
            return
        db.insertar_gasto(detalle, importe, categoria, fecha_modificada)
        print(f"Gasto {detalle} registrado")
    except ValueError:
        print("Escribir los gastos de forma numérica y mayores a 0.")
    except Exception as e:
        print(f"{e}. Error.")

def actualizar_gastos():
    print("MODIFICAR UN GASTO")
    try:
        detalle = input("Que gasto queres modificar? ")
        if not detalle.strip():
            print(f"Ingresó campo vacío")
            return
        if detalle.isnumeric():
            print("Debe ingresar texto")
            return

        nuevo_detalle = input("Ingrese o reescriba el detalle: ")
        nueva_categoria = input("Ingrese o reescriba la categoria: ")
        if not nuevo_detalle.strip() or not nueva_categoria.strip():
            print(f"Ingresó campo vacío")
            return
        if nuevo_detalle.isnumeric() or nueva_categoria.isnumeric():
            print("Debe ingresar texto")
            return
        nuevo_importe = float(input("Ingrese el nuevo importe: "))
        if nuevo_importe <= 0:
            print("El importe de gasto no puede ser 0 o un numero negativo")
            return
        nueva_fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ").strip()
        try:
            fecha_ingresada = date.fromisoformat(nueva_fecha)
        except ValueError:
            print("Ingrese fecha con formato YYYY-MM-DD")
            return
        
        db.actualizar_gasto(nuevo_detalle, nuevo_importe, nueva_categoria, fecha_ingresada, detalle)
        

    except ValueError:
        print("Escribir los gastos de forma numérica y mayores a 0.")
    except Exception as e:
        print(f"{e}. Error.")

def eliminar_gastos():
    print("ELIMINAR UN GASTO")
    try:
        detalle_ingresado = input("Qué gasto quiere eliminar: ").strip()
        if not detalle_ingresado.strip():
            print(f"Ingresó campo vacío")
            return
        if detalle_ingresado.isnumeric():
            print("Debe ingresar texto")
            return
        fecha_ingresada = input("Ingrese la fecha: ").strip()
        if not fecha_ingresada:
            print(f"{fecha_ingresada} no es un dato correcto")
            return
        db.eliminar_gasto(detalle_ingresado, fecha_ingresada)
    except Exception as e:
        print(f"{e}. Error.")

def calcular_total():
    print("CALCULAR TOTAL DE GASTOS INGRESADOS")
    lista = db.ver_gastos()
    if not lista:
        print("No hay gastos registrados para calcular")
    else:
        print("**********************************")
        print("Total de gastos registrados:")
        suma = 0
        for gasto in lista:
            detalle, importe, categoria, fecha = gasto
            suma += importe
        print(f"Total: {suma}")

def calcular_mensual():
    print("CALCULAR TOTAL DE GASTOS MENSUALES")
    mes_ingresado = input("Ingrese el mes del gasto: ")
    mes_formateado = mes_ingresado.zfill(2)
    if int(mes_formateado) < 1 or int(mes_formateado) > 12:
        print(f"No se ingresó un mes correcto: {mes_formateado}")
        return
    anio_ingresado = input("Ingrese el año del gasto: ")
    if int(anio_ingresado) < 2026 or int(anio_ingresado) > 2026:
        print(f"{anio_ingresado} no es un año registrado")
        return
    if not mes_formateado or not anio_ingresado:
        print(f"{mes_formateado} o {anio_ingresado} no son datos correctos")
        return
    else:
        lista = db.ver_mes_anio(mes_formateado, anio_ingresado)
        if not lista:
            print(f"No hay gastos registrados el mes {mes_formateado} de {anio_ingresado}")
        else:
            print("**********************************")
            print(f"Gastos registrados el {mes_formateado} de {anio_ingresado}:")
            suma = 0
            for gasto in lista:
                detalle, importe, = gasto
                suma += importe
                print(f"{detalle}: ${importe}")
            print(f"Total gastos mensuales: {suma}")

def agrupar_categorias():
    print("AGRUPAR GASTOS SEGÚN CATEGORÍA")
    lista = db.ver_gastos()
    if not lista:
        print("No hay gastos registrados para calcular")
    else:
        print("**********************************")
        print("Gastos Y Categorías:")

        lista_importes = []
        lista_categorias = []
        for gasto in lista:
            detalle, importe, categoria, fecha = gasto
            lista_importes.append(importe)
            lista_categorias.append(categoria.title())
    
        dic_categorias = {}
        for indice, categoria in enumerate(lista_categorias):
            importe = lista_importes[indice]

            if categoria in dic_categorias:
                dic_categorias[categoria] += importe
            else: 
                dic_categorias[categoria] = importe

        for categoria, importe in dic_categorias.items():
            print(f"{categoria}: ${importe}")


