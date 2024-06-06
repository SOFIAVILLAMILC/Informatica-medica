import sqlite3 as sql

#crar historial pacientes
def createDB():
    conn=sql.connect("HistorialClinico.db")
    conn.commit()
    conn.close()

def createTable(): #crear tabla de base de datos

    conn = sql.connect("HistorialClinico.db")
    Cursor= conn.cursor()
    Cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS HistorialClinico (
        TI int,
        nombre text ,
        estatura float ,
        peso float ,
        edad int,
        genero text
        )"""
    )
    conn.commit()
    conn.close()
#crear historial examen
def createDB1():
    conn=sql.connect("HistorialExamen.db")
    conn.commit()
    conn.close()

def createTable1():
    conn = sql.connect("HistorialExamen.db")
    Cursor= conn.cursor()
    Cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS HistorialExamen (
        TI int,
        globulos_rojos float,
        globulos_blancos float ,
        plaquetas float ,
        hemoglobina float ,
        hematocrito float,
        Reticulocito float
        )"""
    )

# crear historial medico 
def createDB2():
    conn=sql.connect("HistorialMedico.db")
    conn.commit()
    conn.close() 

def createTable2():
    conn = sql.connect("HistorialMedico.db")
    Cursor= conn.cursor()
    Cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS HistorialMedico (
        usuario text,
        contrasena int
        )"""
    )

def inserRow():#incorporar datos en una fila en la base de datos con una funcion 
        conn= sql.connect("HistorialMedico.db")
        cursor=conn.cursor()     
        intruccion=f"INSERT INTO HistorialMedico(usuario,contrasena) VALUES (?,?);"
        b="laurasofia"
        c=123
        parametro=(b,c)
        cursor.execute(intruccion,parametro)
        conn.commit()
        conn.close()

if __name__=="__main__":
     createDB()
     createTable()
     createDB1()
     createTable1()
     createDB2()
     createTable2()
     inserRow()
     pass
