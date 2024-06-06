
import sqlite3 as sql
from numpy import append

class Usuario:
    def __init__(self):
        self.__usuario = "" 
        self.__contraseña = 0
        
    def AsignarUsuario(self, u):
            self.__usuario = u

    def AsignarContraseña(self, c):
            self.__contraseña = c 
            
    def VerUsuario(self): 
        return self.__usuario 
            
    def VerContraseña(self):
        return self.__contraseña 
            
class Paciente:
    
    def __init__(self,nombre, ti, estatura, peso, edad, genero):
        self.__nombre = nombre
        self.__TI = ti
        self.__estatura = estatura
        self.__peso = peso
        self.__edad = edad
        self.__genero = genero
       
        
    def AsignarNombre(self, n):
        self.__nombre = n 

    def AsignarTI(self, t):
        self.__TI = t 
    
    def AsignarEstatura(self, e):
        self.__estatura = e
    
    def AsignarPeso(self, p):
        self.__peso = p
        
    def AsignarEdad(self, n):
        self.__edad = n
        
    def AsignarGenero(self, n):
        self.__genero = n
    
    def VerNombre(self):
        return self.__nombre 

    def VerTI(self):
        return self.__TI 
    
    def VerEstatura(self):
        return self.__estatura 
    
    def VerPeso(self):
        return self.__peso
    
    def VerEdad(self):
        return self.__edad 

    def VerGenero(self):
        return self.__genero
   
class Examenes:
    def __init__(self,TI,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,conteo_reticulocitos):
        
        self.__TI=TI
        self.__globulos_rojos = globulos_rojos           
        self.__globulos_blancos = globulos_blancos    
        self.__plaquetas = plaquetas     
        self.__hemoglobina = hemoglobina     
        self.__hematocrito = hematocrito    
        self.__conteo_reticulocitos = conteo_reticulocitos  
    
    def aisgnarTI(self,i):
        self.__TI=i

    def asignarRojos(self, r):
            self.__globulos_rojos = r
            
    def asignarBlancos(self, b):
           self.__globulos_blancos = b
           
    def asignarPlaquetas(self, p):
           self.__plaquetas = p   
     
    def asignarHemoglobina(self, h):
       self.__hemoglobina = h
       
    def asignarHematocrito(self, he):
       self.__hematocrito = he
       
    def asignarReticulocito(self, c):
       self.__conteo_reticulocitos = c
    
    def VerTI(self):
        return self.__TI

    def VerRojo(self):
         return self.__globulos_rojos
     
    def VerBlanco(self):
         return self.__globulos_blancos
      
    def VerPlaquetas(self):
         return self.__plaquetas
       
    def VerHemoglobina(self):
        return self.__hemoglobina
        
    def VerHematocrito(self):
        return self.__hematocrito
    
    def VerReticulocito(self):
        return self.__conteo_reticulocitos
    
class sistema:
    
    def __init__(self):
        self.__pin_hospital=123

    def validarUsuarioMed(self, usu,cont ):
        conn=sql.connect("HistorialMedico.db")
        cursor=conn.cursor()
        intruccion=f"SELECT* FROM HistorialMedico WHERE usuario='{usu}'"
        cursor.execute(intruccion)
        datos= cursor.fetchall()
        conn.commit()
        conn.close()
      
        if datos != []: 

            if datos[0][0]== usu and datos [0][1] == int(cont):
                return True

            return False
        return False
    
    def validarUsuarioPac(self,TI):
        conn=sql.connect("HistorialClinico.db")
        cursor=conn.cursor()
        intruccion=f"SELECT* FROM HistorialClinico WHERE TI='{TI}'"
        cursor.execute(intruccion)
        datos= cursor.fetchall()
        conn.commit()
        conn.close()

        if datos != []:
            return True
        
        return False
            
    def validarPin(self,pin):
        return self.__pin_hospital == pin

    def IngresarUsuario(self,usu,cont):

        conn=sql.connect("HistorialMedico.db")
        cursor=conn.cursor()
        intruccion=f"INSERT INTO HistorialMedico(usuario,contrasena) VALUES (?,?);"
        parametro = (usu,cont)
        cursor.execute(intruccion,parametro)
        conn.commit()
        conn.close()

    def IngresarPaciente(self, ti, nombre, estatura, peso, edad, genero):
        conn= sql.connect("HistorialClinico.db")
        cursor=conn.cursor()
        pac = Paciente(nombre, ti, estatura, peso, edad, genero)
        intruccion=f"INSERT INTO HistorialClinico(TI,nombre,estatura,peso,edad,genero) VALUES (?,?,?,?,?,?);"
        parametro=(pac.VerTI(),pac.VerNombre(),pac.VerEstatura(),pac.VerPeso(),pac.VerEdad(),pac.VerGenero())
        cursor.execute(intruccion,parametro)
        conn.commit()
        conn.close()

    def IngresarExamenes(self,TI,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,conteo_reticulocitos):

        conn= sql.connect("HistorialExamen.db")
        cursor=conn.cursor()
        exm = Examenes(TI,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,conteo_reticulocitos)
        instruccion=f"INSERT INTO HistorialExamen(TI,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,Reticulocito) VALUES (?,?,?,?,?,?,?);"
        parametro=(exm.VerTI(),exm.VerRojo(),exm.VerBlanco(),exm.VerPlaquetas(),exm.VerHemoglobina(),exm.VerHematocrito(),exm.VerReticulocito())
      
        cursor.execute(instruccion,parametro)
        conn.commit()
        conn.close()

    def EditarPaciente(self,ti):

        conn=sql.connect("HistorialClinico.db")
        cursor=conn.cursor()
        intruccion=f"SELECT* FROM HistorialClinico WHERE TI='{ti}'"
        cursor.execute(intruccion)
        datos= cursor.fetchall()
        conn.commit()
        conn.close()
        if datos == []:
            return False
        else:
            return datos
    
    def EditarPac(self, ti,nombre, estatura, peso, edad, genero):
        conn=sql.connect("HistorialClinico.db")
        cursor=conn.cursor()
        intruccion="UPDATE HistorialClinico SET nombre=?,estatura=?,peso=?,edad=?,genero=? WHERE TI=?;"
        parametro=(nombre ,estatura, peso, edad, genero,ti)
        cursor.execute(intruccion,parametro)
        cursor.fetchall()
        conn.commit()
        conn.close()
        return True

    def EditarExamenes(self,ti):

        conn=sql.connect("HistorialExamen.db")
        cursor=conn.cursor() #conexion con los comandos SQL
        intruccion=f"SELECT* FROM HistorialExamen WHERE TI='{ti}'" #consulta en el db
        cursor.execute(intruccion)
        datos= cursor.fetchall() #recupera filas y se almacenan en lista de tuplas
        conn.commit() #confirmacion
        conn.close()
       
        if datos == []:
            return False
        else:
            return datos

    def EditarExam(self,ti,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,Reticulocito):
        conn=sql.connect("HistorialExamen.db")
        cursor=conn.cursor()
        intruccion="UPDATE HistorialExamen SET globulos_rojos=?,globulos_blancos=?,plaquetas=?,hemoglobina=?,hematocrito=?,Reticulocito=? WHERE TI=?;"
        parametro=(globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,Reticulocito,ti)
        cursor.execute(intruccion,parametro)
        d=cursor.fetchall()
        conn.commit()
        conn.close()
        return True
        
    def BorrarPaciente(self,ti):
        
        conn= sql.connect("HistorialClinico.db")
        cursor=conn.cursor()
        intruccion=f"DELETE FROM HistorialClinico WHERE TI='{ti}'"
        cursor.execute(intruccion)#un solo insert
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        return True

            
    def BorrarExamen(self,ti):
        conn= sql.connect("HistorialExamen.db")
        cursor=conn.cursor()
        intruccion=f"DELETE FROM HistorialExamen WHERE TI='{ti}'"
        cursor.execute(intruccion)
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
            
    def VerGlobulosRojos(self,edad,globulos_rojos) :

        if edad <= 5:

            if (globulos_rojos>=3.9 and globulos_rojos<=5):
                return " ESTABLE"

            elif (globulos_rojos<3.9):
                return "BAJO"
            
            elif (globulos_rojos>5):
                return "ALTO"

        elif edad >5 and edad <=11:
            
            if (globulos_rojos>=3.9 and globulos_rojos<=5.2):
                return "ESTABLE"

            elif (globulos_rojos<3.9):
                return "BAJO"
            
            elif (globulos_rojos>5.2):
                return "ALTO"

        elif edad >11 and edad <= 17:

            if (globulos_rojos>=4.1 and globulos_rojos<=5.7):
                return "ESTABLE"

            elif (globulos_rojos<4.1):
                return "BAJO"
            
            elif (globulos_rojos>5.7):
                return "ALTO"

    def VerHemoglobina(self,edad,hemoglobina) : 

        if edad <= 5:

            if (hemoglobina>=10.7 and hemoglobina<=14.7):
                return "ESTABLE"

            elif (hemoglobina<10.7):
                return "BAJO"
            
            elif (hemoglobina>14.7):
                return "ALTO"

        elif edad >5 and edad >=11:
            
            if (hemoglobina>=11.1 and hemoglobina<=14.7):
                return "ESTABLE"

            elif (hemoglobina<11.1):
                return "BAJO"
            
            elif (hemoglobina>14.7):
                return "ALTO"
        
        elif edad >11 and edad <= 17:

            if (hemoglobina>=11.7 and hemoglobina<=16.1):
                return "ESTABLE"

            elif (hemoglobina<11.7):
                return "BAJO"
            
            elif (hemoglobina>16.1):
                return "ALTO"

    def VerHematocrito(self,edad,hematocrito) : #porcentaje

        if edad <= 5:

            if (hematocrito>=35 and hematocrito<=42):
                return "ESTABLE"

            elif (hematocrito<35):
                return "BAJO"
            
            elif (hematocrito>42):
                return "ALTO"

        elif edad >5 and edad >=11:

            if (hematocrito>=35 and hematocrito<=47):
                return "ESTABLE"

            elif (hematocrito<35):
                return "BAJO"
            
            elif (hematocrito>47):
                return "ALTO"
        
        elif edad >11 and edad <= 17:

            if (hematocrito>=35 and hematocrito<=48):
                return "ESTABLE"

            elif (hematocrito<35):
                return "BAJO"
            
            elif (hematocrito>48):
                return "ALTO"

    def VerPlaquetas(self,plaquetas) :
       
        if (plaquetas>=150 and plaquetas<= 450): # 10 a ala 3 / ml
            return "ESTABLE"

        elif (plaquetas<150):
            return "BAJO"
            
        elif (plaquetas>450):
            return "ALTO"

    def VerGlobulosBlancos(self,edad,globulos_blancos) :
        
        if edad <= 5:

            if (globulos_blancos>=5 and globulos_blancos<=15.5):#10 ala 3 / ml
                return "ESTABLE"

            elif (globulos_blancos<5):
                return "BAJO"
            
            elif (globulos_blancos>15.5):
                return "ALTO"

        elif edad >5 and edad >=11:

            if (globulos_blancos>=1.5 and globulos_blancos<=13.5):
                return "ESTABLE"

            elif (globulos_blancos<1.5):
                return "BAJO"
            
            elif (globulos_blancos>13.5):
                return "ALTO"
        
        elif edad >11 and edad <= 17:

            if (globulos_blancos>=4.5 and globulos_blancos<=13.5):
                return "ESTABLE"

            elif (globulos_blancos<4.5):
                return "BAJO"
            
            elif (globulos_blancos>13.5):
                return "ALTO"

    def VerReticulocitos(self,conteo_reticulocitos) : 
        if (conteo_reticulocitos>=0.5 and conteo_reticulocitos<=2.5):
            return "ESTABLE"

        elif (conteo_reticulocitos<0.5):
            return "BAJO"
            
        elif (conteo_reticulocitos>2.5):
            return "ALTO"

    def calcularExam(self):
        conn=sql.connect("HistorialExamen.db")
        cursor=conn.cursor()
        intruccion=f"SELECT* FROM HistorialExamen WHERE TI"
        cursor.execute(intruccion)
        datos= cursor.fetchall()
        conn.commit()
        conn.close()
        if datos == []:
            return False
        else:
            lista=[[datos[0][1],datos[0][2],datos[0][3],datos[0][4],datos[0][5],datos[0][6]],["globulos_rojos","globulos_blancos","plaquetas","hemoglobina","hematocrito","Reticulocito"]]

            return lista
    def VerEstadisticas(self): #se define pero no realiza accion
        pass
    
    def calcularExam(self,senal):#leer la tabla de la base de datos 
        conn=sql.connect("HistorialExamen.db")
        cursor=conn.cursor()
        intruccion=f"SELECT* FROM HistorialExamen "
        cursor.execute(intruccion)#un solo insert
        datos= cursor.fetchall()
        conn.commit()
        conn.close()
        conn=sql.connect("HistorialClinico.db")
        cursor=conn.cursor()
        intruccion=f"SELECT* FROM HistorialClinico "
        cursor.execute(intruccion)#un solo insert
        datos1= cursor.fetchall()
        conn.commit()
        conn.close()
        cont=0

        listarojo_5=[]
        listablanco_5=[]      
        listaplaqueta_5=[]
        listahemog_5=[]
        listahemato_5=[]
        listareti_5=[]


        listarojo_11=[]
        listablanco_11=[]
        listaplaqueta_11=[]
        listahemog_11=[]
        listahemato_11=[]
        listareti_11=[]

        listarojo_17=[]
        listablanco_17=[]
        listaplaqueta_17=[]
        listahemog_17=[]
        listahemato_17=[] 
        listareti_17=[]

        listaedad_5=[]
        listaedad_11=[]
        listaedad_17=[]

        cont2=0
        for n in datos1:  #iteracion para clasificacion segun edad
            cont2=cont2+1
            if n[0]==datos1[cont2-1][0]:
                if n[4]<=5:
                    listaedad_5.append([n[0],n[4]])
                elif n[4]>5 and n[4]<=11:
                    listaedad_11.append([n[0],n[4]])
                else:
                    listaedad_17.append([n[0],n[4]])
            else:
                print("no debe")
        
        for i in datos:   #iteracion para promedio de examenes
            cont=cont+1
            cont1=0
            if i[1]== datos[cont-1][1]:
                for e in listaedad_11:
                    cont1=cont1+1
                    if i[0]== listaedad_11[cont1-1][0]:
                        listarojo_11.append(i[1])
                        listablanco_11.append(i[2])
                        listaplaqueta_11.append(i[3])
                        listahemog_11.append(i[4])
                        listahemato_11.append(i[5])
                        listareti_11.append(i[6])
        cont=0
        for i in datos:
            cont=cont+1
            cont1=0
            if i[1]== datos[cont-1][1]:
                for e in listaedad_17:
                    cont1=cont1+1
                    if i[0]== listaedad_17[cont1-1][0]:
                        listarojo_17.append(i[1])
                        listablanco_17.append(i[2])
                        listaplaqueta_17.append(i[3])
                        listahemog_17.append(i[4])
                        listahemato_17.append(i[5])
                        listareti_17.append(i[6])
        cont=0
        for i in datos:
            cont=cont+1
            cont1=0
            if i[1]== datos[cont-1][1]:
                for e in listaedad_5:
                    cont1=cont1+1
                    if i[0]== listaedad_5[cont1-1][0]:
                        listarojo_5.append(i[1])
                        listablanco_5.append(i[2])
                        listaplaqueta_5.append(i[3])
                        listahemog_5.append(i[4])
                        listahemato_5.append(i[5])
                        listareti_5.append(i[6])
               

        prom_rojo_5=sum(listarojo_5)/len(listarojo_5)
        prom_bla_5=sum(listablanco_5)/len(listablanco_5)
        prom_pla_5=sum(listaplaqueta_5)/len(listaplaqueta_5)
        prom_hemog_5=sum(listahemog_5)/len(listahemog_5)
        prom_hemoto_5=sum(listahemato_5)/len(listahemato_5)
        prom_reti_5=sum(listareti_5)/len(listareti_5)

        prom_rojo_11=sum(listarojo_11)/len(listarojo_11)
        prom_bla_11=sum(listablanco_11)/len(listablanco_11)
        prom_pla_11=sum(listaplaqueta_11)/len(listaplaqueta_11)
        prom_hemog_11=sum(listahemog_11)/len(listahemog_11)
        prom_hemoto_11=sum(listahemato_11)/len(listahemato_11)
        prom_reti_11=sum(listareti_11)/len(listareti_11)

        prom_rojo_17=sum(listarojo_17)/len(listarojo_17)
        prom_bla_17=sum(listablanco_17)/len(listablanco_17)
        prom_pla_17=sum(listaplaqueta_17)/len(listaplaqueta_17)
        prom_hemog_17=sum(listahemog_17)/len(listahemog_17)
        prom_hemoto_17=sum(listahemato_17)/len(listahemato_17)
        prom_reti_17=sum(listareti_17)/len(listareti_17)

        listaedad=[len(listaedad_5),len(listaedad_17),len(listaedad_11)]
        total=len(listaedad_5)+len(listaedad_17)+len(listaedad_11)

        if senal== 1:
            return ([prom_rojo_5,prom_bla_5,prom_pla_5,prom_hemog_5,prom_hemoto_5,prom_reti_5],["G.rojos","G.blancos","plaquetas","hemoglobina","hematocrito","Reticulocito"]," 3 - 5 años")
        
        elif senal==2:
            return([prom_rojo_11,prom_bla_11,prom_pla_11,prom_hemog_11,prom_hemoto_11,prom_reti_11],["G.rojos","G.blancos","plaquetas","hemoglobina","hematocrito","Reticulocito"]," 6 - 11 años")
        
        elif senal==3:
            return ([prom_rojo_17,prom_bla_17,prom_pla_17,prom_hemog_17,prom_hemoto_17,prom_reti_17],["G.rojos","G.blancos","plaquetas","hemoglobina","hematocrito","Reticulocito"]," 12 - 17 años")
        
        elif senal==4:
            return (listaedad,["Menores entre 3 - 5 años","Menores entre 6 - 11 años","Menores entre 11 - 17 años"])
        
        elif senal==0:
            return f"Total pacientes registrados: {total}"
    