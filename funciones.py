def leer_archivo(lista):
    with open("gastos.txt", "r") as archivo:
        for linea in archivo:
            lista.append(linea.strip())

def ver_gastos(lista):
    if len(lista) == 0:
        print("No hay gastos registrados")
    else:
        print("Estos son los gastos registrados:")
        for gasto in lista:
            datos = gasto.split(",")
            detalle = datos[0]
            importe = datos[1]
            categoria = datos[2]
            print(f"{detalle}: {importe}")

def agregar_gasto():
    print("Agregar gasto:")
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
    detalle_ingresado = input("Que gasto queres modificar? ")
    nuevo_importe = input("Ingrese el nuevo importe: ")
    categoria_ingresada = input("Ingrese la categoria ")

    with open("gastos.txt", "w") as archivo:
        for gasto in lista:
            datos = gasto.split(",")
            detalle = datos[0]
            importe = datos[1]
            categoria = datos[2]
            if detalle_ingresado == detalle:
                producto_modificado = f"{detalle}, {nuevo_importe}, {categoria}\n"
                archivo.write(producto_modificado)
            else:
                producto = f"{detalle}, {importe}, {categoria}\n"
                archivo.write(producto)

def eliminar_gastos(lista):
    if len(lista) == 0:
        print("No hay gastos para eliminar")
        return
    else:
        print("Eliminar un gasto")
        detalle_ingresado = input("Qué gasto quiere eliminar: ")
        with open("gastos.txt", "w") as archivo:
            for gasto in lista:
                datos = gasto.split(",")
                detalle = datos[0]
                if detalle_ingresado != detalle:
                    archivo.write(gasto + "\n")


# def ver_gastos():
#     print("Estos son los gastos registrados:")
#     gasto = 0
#     if len(lista_gastos) == 0:
#         print("No hay gastos registrados")
#     else:
#         for x, y in lista_gastos.items():
#             print(f"{x}: {y}")



# def agregar_gasto():
#     try:
#         detalle = input("Ingrese el detalle del gasto: ")
#         gasto = float(input("Ingrese el importe del gasto: "))
#         if gasto <= 0:
#             raise ValueError("El importe de gasto no puede ser 0 o un numero negativo")
#         lista_gastos[detalle] = gasto
#         print("Importe ingresado correctamente.")
#     except ValueError:
#         print("Excribir los gastos de forma numérica y mayores a 0.")
#     except Exception as e:
#         print(f"{e}. Error.")

# def actualizar_gastos():
#     if len(lista_gastos) == 0:
#         print("No hay datos para modificar")
#         return
#     else: 
#         detalle = input("Que gasto queres modificar? ")
#         if detalle in lista_gastos:
#             nuevo_detalle = input(("Cual es el nuevo detalle? Si es el mismo escribilo nuevamente "))
#             if nuevo_detalle.isalpha():
#                 lista_gastos[nuevo_detalle] = lista_gastos.pop(detalle)
#             else:
#                 print("El detalle no debe ser numerico")
#                 return
#             try:
#                 nuevo_gasto = float(input("Cual es el nuevo gasto? Si es el mismo escribilo nuevamente "))
#                 lista_gastos[nuevo_detalle]= nuevo_gasto
#             except ValueError:
#                 print("El gasto debe ser numerico")
#         else:
#             print("Ese detalle no está registrado")

# def eliminar_gastos():
#     while True:
#         try:
#             if len(lista_gastos) == 0:
#                 print("No hay gastos para eliminar")
#                 break
#             else:
#                 detalle = input("Qué gasto quiere eliminar: ")
#                 if detalle in lista_gastos:
#                     lista_gastos.pop(detalle)
#                     print("Gasto eliminado ok")
#                     break
#                 else:
#                     print("Ese gasto no está en tu lista")
#                     break
#         except ValueError:
#             print("No ingreso un numero de gasto")
#         except Exception as e:
#             print("Error. No se ingresó un número")

