import sqlite3

db = 'registro_gastos.db'

tabla = [

]

def conexion():
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


conexion()