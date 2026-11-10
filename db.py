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

def insertar_gasto(conexion, gasto):
    sql = '''INSERT INTO gastos (detalle, importe, categoria, fecha)
            VALUES(?, ?, ?, ?)'''

    cur = conexion.cursor()
    cur.execute(sql, gasto)
    conexion.commit()

    return cur.lastrowid

crear_db()