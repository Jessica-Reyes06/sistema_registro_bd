import os
import mysql.connector

# Leer contraseña desde variable de entorno
password = os.getenv("MYSQL_PASSWORD")

# Conexión única y compartida a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="control_escolar"
)

print("Conectado a MySQL (db_conexion)")


def ejecutar_insert(sql, datos):
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()


def ejecutar_select(sql, params=None):
    cursor = conexion.cursor()
    if params is None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, params)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
