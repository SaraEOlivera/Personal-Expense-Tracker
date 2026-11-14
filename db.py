import sqlite3

def crear_db():
    try:
        with sqlite3.connect('bd/registro_gastos.db') as conexion:
            cursor = conexion.cursor()

            cursor.execute(
                    """CREATE TABLE IF NOT EXISTS gastos (
                        id INTEGER PRIMARY KEY,
                        detalle TEXT NOT NULL,
                        importe REAL NOT NULL,
                        categoria TEXT NOT NULL,
                        fecha DATE
                    ); """
            )
            print("La tabla se creó")
            conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"Error al crear la tabla {e}")

def insertar_gasto(detalle, importe, categoria, fecha):
    try:
        with sqlite3.connect("bd/registro_gastos.db") as conexion:
            cur = conexion.cursor()
            cur.execute('''INSERT INTO gastos (detalle, importe, categoria, fecha)
                    VALUES(?, ?, ?, ?)''', (detalle, importe, categoria, fecha))
            conexion.commit()

            return cur.lastrowid
    
    except sqlite3.IntegrityError as e:
        print(f"Error en la restriccion de integridad de la BD {e}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos {e}")

def ver_gastos():
    try:
        with sqlite3.connect("bd/registro_gastos.db") as conexion:
            cur = conexion.cursor()
            cur.execute('SELECT detalle, importe, categoria, fecha FROM gastos')
            filas = cur.fetchall()
            # for fila in filas:
            #     print(fila)
            return filas
    except sqlite3.OperationalError as e:
        print(f"Error al ejecutar la operacion: {e}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos {e}")

def ver_un_gasto(fecha):
    try:
        with sqlite3.connect("bd/registro_gastos.db") as conexion:
            cur = conexion.cursor()
            cur.execute('SELECT detalle, importe, categoria, fecha FROM gastos WHERE fecha = ?', (fecha,))
            fila = cur.fetchall()
            return fila
    except sqlite3.OperationalError as e:
        print(f"Error al ejecutar la operacion: {e}")
    except sqlite3.Error as e:
        print(f"Error en la base de datos {e}")

def actualizar_gasto(detalle_nuevo, importe, categoria, fecha, detalle):
    try:
        with sqlite3.connect("bd/registro_gastos.db") as conexion:   
            cur = conexion.cursor()
            cur.execute('''UPDATE gastos
            SET  detalle=?, importe=?, categoria=?, fecha=?
            WHERE detalle = ?  ''',( detalle_nuevo, importe, categoria, fecha, detalle))
            conexion.commit()
        print(f"{cur.rowcount} filas modificadas")
    except sqlite3.Error as e:
        print(f"Error en la base de datos {e}")

def eliminar_gasto(detalle):
    try:
        with sqlite3.connect("bd/registro_gastos.db") as conexion:   
            cur = conexion.cursor()
            cur.execute('''DELETE FROM gastos
            WHERE detalle = ?  ''', (detalle,))
            conexion.commit()
            print(f"{cur.rowcount} filas modificadas")
    except sqlite3.Error as e:
        print(f"Error en la base de datos {e}")




