# def leer_archivo(lista):
#     with open("gastos.txt", "r") as archivo:
#         for linea in archivo:
#             lista.append(linea.strip())
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
    lista = db.ver_un_gasto(fecha_ingresada)
    if not lista:
        print("No hay gastos registrados")
    else:
        print("Ver gastos guardados en una fecha")
        fecha_ingresada = input("Ingrese la fecha:")
        if not fecha_ingresada:
            print(f"No se registraron gastos el {fecha_ingresada}")
        else:
            print("**********************************")
            print(f"Estos son los gastos registrados el {fecha_ingresada}:")
            for gasto in lista:
                detalle, importe, categoria, fecha = gasto
                print(f"{detalle}: {importe} categoria: {categoria} - {fecha}")


def agregar_gasto():
    print("AGREGAR GASTO:")
    try:
        detalle = input("Ingrese el detalle del gasto: ")
        categoria = input("Ingrese categoria del gasto: ")
        if detalle.isnumeric() or categoria.isnumeric():
            print("Debe ingresar texto")
            return
        importe = int(input("Ingrese el importe del gasto: "))
        if importe <= 0:
            print("El importe de gasto no puede ser 0 o un numero negativo")
            return
        nuevo_gasto = f"{detalle}, {importe}, {categoria}\n"
        with open("gastos.txt", "a") as archivo:
            archivo.write(nuevo_gasto)
    except ValueError:
        print("Escribir los gastos de forma numérica y mayores a 0.")
    except Exception as e:
        print(f"{e}. Error.")

def actualizar_gastos(lista):
    print("Modificar un gasto - solo el importe")
    if len(lista) == 0:
        print("No hay gastos registrados para modificar.")
    else:
        try:
            detalle_ingresado = input("Que gasto queres modificar? ")
            if detalle_ingresado.isnumeric():
                print("Debe ingresar texto")
                return
            nuevo_importe = int(input("Ingrese el nuevo importe: "))

            if nuevo_importe <= 0:
                print("El importe de gasto no puede ser 0 o un numero negativo")
                return
            encontrado = False
            with open("gastos.txt", "w") as archivo:
                for gasto in lista:
                    datos = gasto.split(",")
                    detalle = datos[0]
                    importe = datos[1]
                    categoria = datos[2]
                    if detalle_ingresado == detalle:
                        encontrado = True
                        producto_modificado = f"{detalle}, {nuevo_importe}, {categoria}\n"
                        archivo.write(producto_modificado)
                    else:
                        producto = f"{detalle}, {importe}, {categoria}\n"
                        archivo.write(producto)
            if encontrado:
                print("Gasto modificado")
            else:
                print("Ese gasto no está registrado")
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


