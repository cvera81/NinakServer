# -*- coding: utf-8 -*-
import sys
import pymysql


DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = '123456' 
DB_NAME = 'ninal'
 
def run_query(query,data):
    
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = pymysql.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor
    if data == "":
        cursor.execute(query) # Ejecutar una consulta 
    else:
        cursor.execute(query,data) # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor   # Traer los resultados de un select 
    else: 
        conn.commit()   # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()      # Cerrar el cursor 
    conn.close()        # Cerrar la conexión 
 
    return data