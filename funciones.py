from datetime import date
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
            print(f"{detalle}: {importe} categoria: {categoria} - {fecha}")

def ver_un_gasto():
    print("VER GASTO REGISTRADO")
    fecha_ingresada = input("Ingrese la fecha:")
    if not fecha_ingresada:
        print(f"{fecha_ingresada} no es un dato correcto")
        return
    else:
        lista = db.ver_un_gasto(fecha_ingresada)
        print("**********************************")
        print(f"Estos son los gastos registrados el {fecha_ingresada}:")
        if not lista:
                print(f"No hay gastos registrados el {fecha_ingresada}")
        else:
            for gasto in lista:
                detalle, importe, categoria, fecha = gasto
                print(f"{detalle}: {importe} categoria: {categoria} - {fecha}")

def agregar_gasto():
    print("AGREGAR UN GASTO:")
    try:
        detalle = input("Ingrese el detalle del gasto: ")
        categoria = input("Ingrese categoria del gasto: ")
        if not detalle or not categoria:
            print(f"Ingresó campo vacío")
            return
        elif detalle.isnumeric() or categoria.isnumeric():
            print("Debe ingresar texto")
            return
        importe = float(input("Ingrese el importe del gasto: "))
        if importe <= 0:
            print("El importe de gasto no puede ser 0 o un numero negativo")
            return
        fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ").strip()
        try:
            fecha_ingresada = date.fromisoformat(fecha)
        except ValueError:
            print("Ingrese fecha con formato YYYY-MM-DD")
            return
        db.insertar_gasto(detalle, importe, categoria, fecha_ingresada)
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

def eliminar_gastos(lista):
    if len(lista) == 0:
        print("No hay gastos para eliminar")
        return
    else:
        print("Eliminar un gasto")
        detalle_ingresado = input("Qué gasto quiere eliminar: ")

        encontrado = False
        with open("gastos.txt", "w") as archivo:
                for gasto in lista:
                    datos = gasto.split(",")
                    detalle = datos[0]
                    if detalle_ingresado != detalle:
                        archivo.write(gasto + "\n")
                    else:
                        encontrado = True
        if encontrado:
            print("Gasto eliminado")
        else:
            print("Gasto no registrado")

def calcular_total(lista):
    if len(lista) == 0:
        print("No hay gastos registrados para sumar")
        return
    else:
        print("**********************************")
        print("Este es el total de tus gastos registrados:")
        suma = 0
        for gasto in lista:
            datos = gasto.split(",")
            importe = datos[1]
            importe_numero = float(importe)
            suma += importe_numero
    print(f"Total: {suma}")

def agrupar_categorias(lista):
    if len(lista) == 0:
        print("No hay gastos registrados")
    else:
        print("**********************************")
        print("Estos son los gastos por categorías:")
        lista_importes = []
        lista_categorias = []
        for gasto in lista:
            datos = gasto.split(",")
            importe = datos[1]
            categoria = datos[2]
            lista_importes.append(int(importe))
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


