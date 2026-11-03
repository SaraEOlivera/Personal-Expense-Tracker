def leer_archivo(lista):
    with open("gastos.txt", "r") as archivo:
        for linea in archivo:
            lista.append(linea.strip())

def ver_gastos(lista):
    if len(lista) == 0:
        print("No hay gastos registrados")
    else:
        print("**********************************")
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
    try:
        detalle_ingresado = input("Que gasto queres modificar? ")
        # categoria_ingresada = input("Ingrese la categoria ")
        if detalle_ingresado.isnumeric():
            print("Debe ingresar texto")
            return
        if detalle_ingresado in lista:
            print("Gasto modificado")
        else: 
            print("Ese gasto no está registrado")
            return
        nuevo_importe = int(input("Ingrese el nuevo importe: "))
        if nuevo_importe <= 0:
            print("El importe de gasto no puede ser 0 o un numero negativo")
            return
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
        encontrado = True
        for i in range(len(lista)):
            if detalle_ingresado in lista[i]:
                encontrado = True
            else:
                encontrado = False
        if encontrado:
            print("Gasto eliminado")
        else:
            print("Gasto no registrado")

        with open("gastos.txt", "w") as archivo:
                for gasto in lista:
                    datos = gasto.split(",")
                    detalle = datos[0]
                    if detalle_ingresado != detalle:
                        archivo.write(gasto + "\n")

