import sqlite3
from tabulate import tabulate

class Data_base():
    @staticmethod
    def crear_db():
        with sqlite3.connect("DEEP DIVE - SUBMARINE SOS/database/puntuaciones.db") as conexion:
            try:
                sentencia = """CREATE TABLE IF NOT EXISTS puntuaciones
                                (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre VARCHAR(100) NOT NULL,
                                    score INT NOT NULL 
                                )"""
                conexion.execute(sentencia)
                print("La tabla se creó exitosamente")
            except sqlite3.OperationalError:
                print("La tabla ya estaba creada")

    @staticmethod
    def insertar_datos_db(nombre, score):
        # Insertar datos en la tabla
        with sqlite3.connect("DEEP DIVE - SUBMARINE SOS/database/puntuaciones.db") as conexion:
            try:
                conexion.execute("INSERT INTO puntuaciones (nombre, score) VALUES (?, ?)", (nombre, score))
                conexion.commit()
                print(f"Datos insertados correctamente\nNombre: {nombre}\nScore: {score}")
            except sqlite3.Error as e:
                print("Error:", e)

    @staticmethod
    def eliminar_datos_db(nombre):
        with sqlite3.connect("DEEP DIVE - SUBMARINE SOS/database/puntuaciones.db") as conexion:
            try:
                conexion.execute("DELETE FROM puntuaciones WHERE nombre = ?", (nombre,))
                conexion.commit()
                print(f"Datos eliminados correctamente.\n{nombre}")
            except sqlite3.Error as e:
                print("Error:", e)

    @staticmethod
    def recuperar_datos_db():
        #recuperar datos
        with sqlite3.connect("DEEP DIVE - SUBMARINE SOS/database/puntuaciones.db") as conexion:
            cursor = conexion.execute("SELECT * FROM puntuaciones")
            lista_salida = []
            for fila in cursor:
                dict_datos = {
                    "id": fila[0],
                    "nombre": fila[1],
                    "score": fila[2]
                }
                lista_salida.append(dict_datos)

            return lista_salida

#Data_base.crear_db()
#eliminar_datos_db("José")
#insertar_datos_db("Roberto", 1000)
#print(tabulate(recuperar_datos_db(), headers="keys"))