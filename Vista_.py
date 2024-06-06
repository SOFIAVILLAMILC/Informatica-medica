# Vista


from Modelo_ import Paciente, Examenes
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog,QMessageBox,QGraphicsGridLayout,QVBoxLayout
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtCore import Qt,QRegExp,QEvent
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np



class MenuPPal(QMainWindow):
    
    def __init__(self):
        super(MenuPPal,self).__init__()
        loadUi("MenuPrincipal.ui",self)
        self.setUp() 
        
    def setUp(self):
        
        self.Bot_Paciente.clicked.connect(self.Menu_Paciente)
        self.Bot_Doctor.clicked.connect(self.Menu_Doctor)      
        self.Bot_Salir.clicked.connect(self.salir)
        
    def Menu_Doctor(self):
        
        vim= VentanaIngresarUsuarioDoc(self)
        vim.setControl(self.__control)
        vim.show()
        self.hide()
        
    def Menu_Paciente(self):
        
        vbp= VentanaIngresarUsuarioPac(self)
        vbp.setControl(self.__control)
        vbp.show()
        self.hide()
        
    def salir(self):
        
        m = QMessageBox.question(self,"¿Seguro?","Seguro desea salir del aplicativo")
        if m == QMessageBox.Yes:
            self.close()  
        
    def setControl(self,c):
        self.__control = c
                
           
class VentanaIngresarUsuarioPac(QDialog):
    
    def __init__(self, ppal = None): 

        super(VentanaIngresarUsuarioPac, self).__init__(ppal)
        loadUi('BuscarPaciente.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
        
        
    def setUp(self):
        
        self.TI.setValidator(QIntValidator())
        self.buscar.clicked.connect(self.Ingreso)
        self.salir.clicked.connect(self.exit)
        
    def Ingreso(self):
        TI= self.TI.text()
        result=self.__control.validarUsuarioPac(TI)
        if result == True:
            pac= VentanaMenuPac(self)
            pac.setControl(self.__control)
            pac.show()
            self.hide()

        else:
            msg= QMessageBox.information(self, "Alerta", "El usuario es incorrecto")
    
    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close() 
              
    def setControl(self,c):
        self.__control = c

class VentanaMenuPac(QDialog):

    def __init__(self, ppal = None): 
        super(VentanaMenuPac, self).__init__(ppal)
        loadUi('MenuPaciente.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
           
    def setUp(self):

        self.Ver_Diagnostico.clicked.connect(self.diagnostico)
        self.Ver_Estadisticas.clicked.connect(self.estadistica)
        self.salir.clicked.connect(self.exit)
    
    def diagnostico(self): #aqui visualizo el paciente del que ingreso el id
        dig=VentanaBuscarPacienteDiag(self)
        dig.setControl(self.__control)
        dig.show()
        self.hide()

    def estadistica(self): #aqui miro estadistica en donde estoy resto de pacientes
        est= VentanaEstadistica(self)
        est.setControl(self.__control)
        est.mostrar()
        est.show()
        self.hide()

    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close() 

    def setControl(self,c):
        self.__control = c 

class VentanaIngresarUsuarioDoc(QDialog):
    
    def __init__(self, ppal = None): 

        super(VentanaIngresarUsuarioDoc, self).__init__(ppal)
        loadUi('IngresarUsuario.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
           
    def setUp(self):

        self.Bot_Usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+"))) #cadena regular de miniscula y mayuscula
        self.Bot_Contrasena.setValidator(QIntValidator())
        self.ingresar.clicked.connect(self.Ingresar_Usuario)
        self.salir.clicked.connect(self.exit)
        self.Bot_Crear.clicked.connect(self.Crear_Usuario)

    def Ingresar_Usuario(self):
    
        usuario= self.Bot_Usuario.text()
        contrasena= self.Bot_Contrasena.text()
        result=self.__control.validarUsuarioMed(usuario,contrasena)
    
        if result == True:
            vmd= VentanaMenuDoctor(self)
            vmd.setControl(self.__control)
            vmd.show()
            self.hide()

        else:
            msg= QMessageBox.information(self, "Alerta", "El usuario es incorrecto")
        
    def Crear_Usuario(self):
        
        vcu= VentanaPin(self)
        vcu.setControl(self.__control)
        vcu.show()
        self.hide()

    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close()    
                 
    def setControl(self,c):
        self.__control = c


class VentanaPin(QDialog):
    def __init__(self, ppal = None): 

        super(VentanaPin, self).__init__(ppal)
        loadUi('pin.ui', self)
        self.__MenuPPal = ppal
        self.setUp()

    def setUp(self):  

        self.pin.setValidator(QIntValidator())
        self.ingresar.clicked.connect(self.ingreso)
        self.salir.clicked.connect(self.exit)

    def ingreso(self):
        pin= self.pin.text()
        if str(pin)!="":
            result=self.__control.validarPin(int(pin))
            if result == True:
                vmd= VentanaCrearUsuarioDoc(self)
                vmd.setControl(self.__control)
                vmd.show()
                self.hide()

            else:
                msg= QMessageBox.information(self, "Alerta", "El usuario es incorrecto")
        else:
            msg= QMessageBox.information(self, "Alerta", "Rellene todos los campos")
    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close()

    def setControl(self,c):
        self.__control = c

class VentanaCrearUsuarioDoc(QDialog):

    def __init__(self, ppal = None): 

        super(VentanaCrearUsuarioDoc, self).__init__(ppal)
        loadUi('CrearUsuario.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
        
    def setUp(self):

        self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.contrasena.setValidator(QIntValidator())
        self.crear.clicked.connect(self.Crear_Usuario)
        self.salir.clicked.connect(self.exit)
        
    
    def Crear_Usuario(self):

        usu=self.usuario.text()
        cont=self.contrasena.text()
        result=self.__control.validarUsuarioMed(usu,cont)
        if result == True:
            msg= QMessageBox.information(self, "Alerta", "El usuario ya esta registrado en el sistema")

        else:
            if usu!="" and str(cont)!="":
                self.__control.IngresarUsuario(usu,cont)
                msg= QMessageBox.information(self, "Alerta", "Usuario registrado con exito ")
            else:
                msg= QMessageBox.information(self, "Alerta", "Rellene todos los campos")

    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close()
           
            
    def setControl(self,c):
        self.__control = c
        
        
class VentanaMenuDoctor(QDialog):
    
    def __init__(self, ppal = None): 

        super(VentanaMenuDoctor, self).__init__(ppal)
        loadUi('MenuDoctor.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
        
    def setUp(self):
        
        self.Ing_Paciente.clicked.connect(self.Ingresar_Paciente)
        self.Edi_Paciente.clicked.connect(self.Editar_Paciente)
        self.Eli_Paciente.clicked.connect(self.Eliminar_Paciente)
        self.Ver_Diagnostico.clicked.connect(self.V_Diagnostico)
        self.Ver_Estadisticas.clicked.connect(self.V_Estadisticas)
        
        self.Bot_Salir2.clicked.connect(self.salir)
        
    def Ingresar_Paciente(self):
        
        vip= VentanaIngresarPaciente(self)
        vip.setControl(self.__control)
        vip.show()
        self.hide()
    
    def Editar_Paciente(self):
        
        vbp= VentanaBuscarPacienteEdit(self)
        vbp.setControl(self.__control)
        vbp.show()
        self.hide()

    def Eliminar_Paciente(self):
        
        vbp= VentanaBuscarPacienteEliminar(self)
        vbp.setControl(self.__control)
        vbp.show()
        self.hide()
    
    def V_Diagnostico(self):
        dig=VentanaBuscarPacienteDiag(self)
        dig.setControl(self.__control)
        dig.show()
        self.hide() 

    def V_Estadisticas(self):
        est= VentanaEstadistica(self)
        est.setControl(self.__control)
        est.mostrar()
        est.show()
        self.hide()

    def salir(self):
        pl =self.__MenuPPal
        pl.show()
        self.close()
        
    def setControl(self,c):
        self.__control = c

class VentanaIngresarPaciente(QDialog):
    def __init__(self, ppal = None): 
        super(VentanaIngresarPaciente, self).__init__(ppal)
        loadUi('IngresarPaciente.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
        
    def setUp(self):
         
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_ti.setValidator(QIntValidator())
        self.campo_estatura.setValidator(QDoubleValidator())
        self.campo_peso.setValidator(QDoubleValidator())
        self.ingresar.clicked.connect(self.Ingresar_Examenes)
        self.salir.clicked.connect(self.exit)
        
     
    def Ingresar_Examenes(self):
        
        nombre = self.campo_nombre.text()
        ti = self.campo_ti.text()
        estatura = self.campo_estatura.text()
        peso = self.campo_peso.text()
        edad = self.campo_edad.itemText(self.campo_edad.currentIndex())
        genero = self.campo_sexo.itemText(self.campo_sexo.currentIndex())
        result= self.__control.validarUsuarioPac(ti)

        if result == False:
            if (nombre != "" and str(estatura))!="" and (str(ti)!="" and str(peso) !=""):

                vie= VentanaIngresarExamenes(self)
                vie.setControl(self.__control)
                vie.guardarTI(ti,nombre, estatura, peso, edad, genero)
                vie.show()
                self.hide()
            
            else:
                msg= QMessageBox.information(self, "Alerta", "Rellene todos los campos")
        else :
            msg= QMessageBox.information(self, "Alerta", "El paciente ya se encuentra registrado")

    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close()
    
    def setControl(self,c):
        self.__control = c  


class VentanaIngresarExamenes(QDialog):

    def __init__(self, ppal = None): 
        super(VentanaIngresarExamenes, self).__init__(ppal)
        loadUi('IngresarExamenes.ui', self)
        self.__MenuPPal= ppal
        self.setUp()
        self.TI=[]
    
    def guardarTI(self,TI,nombre, estatura, peso, edad, genero):
        self.TI=[TI,nombre, estatura, peso, edad, genero]

    def verTI(self):  
        return self.TI[0]
    
    def verNombre(self):
        return self.TI[1]
    
    def verEstatura(self):
        return self.TI[2]
    
    def verPeso(self):
        return self.TI[3]
    
    def verEdad(self):
        return self.TI[4]

    def verGenero(self):
        return self.TI[5]

    def eliminarTI(self):
        self.TI.clear()

    def setUp(self):
         
        self.campo_gr.setValidator(QDoubleValidator())
        self.campo_gb.setValidator(QDoubleValidator())
        self.campo_plaq.setValidator(QDoubleValidator())
        self.campo_hemat.setValidator(QDoubleValidator())
        self.campo_hemog.setValidator(QDoubleValidator())
        self.campo_ret.setValidator(QDoubleValidator())
        self.salir.clicked.connect(self.exit)
        self.registrar.clicked.connect(self.aceptar)
        
    def aceptar(self):
           
        #ingresa examen
        globulos_rojos = self.campo_gr.text() 
        globulos_blancos = self.campo_gb.text() 
        plaquetas = self.campo_plaq.text()
        hematocrito  = self.campo_hemat.text()
        hemoglobina = self.campo_hemog.text()
        conteo_reticulocitos = self.campo_ret.text()

        ti = self.verTI()
        nombre = self.verNombre()
        estatura= self.verEstatura()
        peso= self.verPeso()
        edad = self.verEdad()
        genero= self.verGenero()
        if (str(globulos_rojos) != "" and str(globulos_blancos)!="") and (str(hematocrito)!="" and (str(plaquetas) and (str(conteo_reticulocitos!="") and (str(hemoglobina!=""))))):
            self.eliminarTI()

            self.__control.IngresarPaciente(ti, nombre, estatura, peso, edad, genero)
            self.__control.IngresarExamenes(ti,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,conteo_reticulocitos)
            pl=self.__MenuPPal
            msg = QMessageBox.information(self,"Alerta", "Paciente ingresado con exito")
            pl.show()
            self.hide()
            #self.close()

        else:
            msg= QMessageBox.information(self, "Alerta", "Rellene todos los campos")
   
    def exit(self):
        pl =self.__MenuPPal
        pl.show()
        self.close()
           
    def setControl(self,c):
        self.__control = c  


class VentanaBuscarPacienteEliminar(QDialog):
    
    def __init__(self, ppal = None): 
        super(VentanaBuscarPacienteEliminar, self).__init__(ppal)
        loadUi('BuscarPaciente.ui', self)
        self.__mainWindow = ppal
        self.setUp()

    def setUp(self):
        
        self.buscar.clicked.connect(self.Ingreso)
        self.salir.clicked.connect(self.exit)
        
    def Ingreso(self):

        Ti=self.TI.text()     
        result=self.__control.validarUsuarioPac(Ti)

        if result:
            self.__control.BorrarPaciente(Ti)
            self.__control.BorrarExamen(Ti)
            msg = QMessageBox.information(self,"Alerta", "Paciente eliminado con exito")

        else : 
            msg=QMessageBox.information(self,"Alerta", "Paciente no encontrado")
        
    
    def exit(self):
        self.__mainWindow.show()
        self.hide()
        
           
    def setControl(self,c):
        self.__control = c
        

class VentanaBuscarPacienteEdit(QDialog):#esta me lleva a editar
    def __init__(self, ppal = None): 
        super(VentanaBuscarPacienteEdit, self).__init__(ppal)
        loadUi('BuscarPaciente.ui', self)
        self.__MenuPPal = ppal
        self.setUp()

    def setUp(self):
        
        self.TI.setValidator(QIntValidator())
        self.buscar.clicked.connect(self.Ingreso)
        self.salir.clicked.connect(self.exit)
        
    def Ingreso(self):
        TI= self.TI.text()
        result=self.__control.validarUsuarioPac(TI)

        if result == True:
            pac= VentanaEditarPaciente(self)
            pac.guardarTI(TI)
            pac.setControl(self.__control)
            pac.show()
            self.hide()

        else:
            msg= QMessageBox.information(self, "Alerta", "El usuario no existe")

    def exit(self):
         self.__MenuPPal.show()
         self.hide()
                   
    def setControl(self,c):
        self.__control = c        

                
class VentanaEditarPaciente(QDialog):

    def __init__(self, ppal = None): 
        super(VentanaEditarPaciente, self).__init__(ppal)
        loadUi('EditarPaciente.ui', self)
        self.__MenuPPal= ppal
        self.setUp()
        self.TI=[]
        
    def setUp(self):
         
        self.campo_nombre_.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_estatura_.setValidator(QDoubleValidator())
        self.campo_peso_.setValidator(QDoubleValidator())
        self.examen.clicked.connect(self.examenes)
        self.salir.clicked.connect(self.exit)
        self.boton_editar.clicked.connect(self.Editar_Pac)
    
    def guardarTI(self,TI):
        self.TI=[TI]

    def eliminarTI(self):
        self.TI.clear()
    
    def verTI(self):
        return self.TI[0]

    def examenes(self):
        ti = self.verTI()
        vie= VentanaEditarExamenes(self)
        vie.setControl(self.__control)
        vie.guardarTI(ti)
        vie.show()
        self.hide()

    def Editar_Pac(self):
        #funcion 
        nombre = self.campo_nombre_.text()
        estatura = self.campo_estatura_.text()
        peso = self.campo_peso_.text()#campo_edad_
        edad = self.campo_edad_.itemText(self.campo_edad_.currentIndex())
        genero = self.campo_sexo_.itemText(self.campo_sexo_.currentIndex())

        
        ti = self.verTI()
        ti1 = self.__control.EditarPaciente(ti)
        lista= [nombre,estatura,peso,edad,genero]

        for n in lista:
            if ""==n and n==nombre:
                nombre = ti1[0][1]
            elif ""==n and n==edad:
                edad = ti1[0][4]
            elif ""==n and n==estatura:
                estatura = ti1[0][2]
            elif ""==n and n==peso:
                peso=ti1[0][3]
            elif ""==n and n== genero:
                genero=ti1[0][5]
        
        result = self.__control.EditarPac(ti,nombre, estatura, peso, edad, genero)

        if result:
            msg = QMessageBox.information(self, "Alerta", "Paciente modificado")
            

    def exit(self):
         self.eliminarTI()
         self.__MenuPPal.show()
         self.hide()
        
    def setControl(self,c):
        self.__control = c  
        
class VentanaEditarExamenes(QDialog):
    
    def __init__(self, ppal = None): 
        super(VentanaEditarExamenes, self).__init__(ppal)
        loadUi('IngresarExamenes.ui', self)
        self.__mainWindow = ppal
        self.setUp()
        self.TI=[]

    def guardarTI(self,TI):
        self.TI=[TI]

    def eliminarTI(self):
        self.TI.clear()
    
    def verTI(self):
        return self.TI[0]  
    def setUp(self):
         
        self.campo_gr.setValidator(QDoubleValidator())
        self.campo_gb.setValidator(QDoubleValidator())
        self.campo_plaq.setValidator(QDoubleValidator())
        self.campo_hemat.setValidator(QDoubleValidator())
        self.campo_hemog.setValidator(QDoubleValidator())
        self.campo_ret.setValidator(QDoubleValidator())
        self.registrar.clicked.connect(self.aceptar)
        self.salir.clicked.connect(self.exit)
        
    def aceptar(self):

        globulos_rojos = self.campo_gr.text() 
        globulos_blancos = self.campo_gb.text() 
        plaquetas = self.campo_plaq.text()
        hematocrito  = self.campo_hemat.text()
        hemoglobina = self.campo_hemog.text()
        conteo_reticulocitos = self.campo_ret.text()

        ti = self.verTI()
        ti1 = self.__control.EditarExamenes(ti)

        lista= [ globulos_rojos,globulos_blancos,plaquetas, hematocrito,hemoglobina,conteo_reticulocitos]

        for n in lista:

            if ""==n and n==globulos_rojos:
                globulos_rojos = ti1[0][1]
            elif ""==n and n==hematocrito:
                hematocrito= ti1[0][4]
            elif ""==n and n==globulos_blancos:
                globulos_blancos = ti1[0][2]
            elif ""==n and n==plaquetas:
                plaquetas=ti1[0][3]
            elif ""==n and n== hemoglobina:
                hemoglobina=ti1[0][5]
            elif ""==n and n== conteo_reticulocitos:
                conteo_reticulocitos=ti1[0][6]

        self.eliminarTI()
        result = self.__control.EditarExam(ti,globulos_rojos,globulos_blancos,plaquetas, hematocrito,hemoglobina,conteo_reticulocitos)
       
        if result:
            msg = QMessageBox.information(self, "Alerta", "Se ha modificado con exito")
            self.__mainWindow.show()
            self.hide()
    def exit(self):
         self.__mainWindow.show()
         self.hide()
          
    def setControl(self,c):
        self.__control = c  
        
class VentanaBuscarPacienteDiag(QDialog):
    def __init__(self, ppal = None): 

        super(VentanaBuscarPacienteDiag, self).__init__(ppal)
        loadUi('BuscarPaciente.ui', self)
        self.__MenuPPal = ppal
        self.setUp()

    def setUp(self):
        
        self.TI.setValidator(QIntValidator())
        self.buscar.clicked.connect(self.Ingreso)
        self.salir.clicked.connect(self.exit)

    def Ingreso(self):
        Ti=self.TI.text()     
        result=self.__control.validarUsuarioPac(Ti)

        if result:

            dig=VentanaDiagnostico(self)
            dig.setControl(self.__control)
            dig.guardarTI(Ti)
            dig.visualizar()
            dig.show()
            self.hide()

        else : 
            msg=QMessageBox.information(self,"Alerta", "Paciente no encontrado")

    def exit(self):
         
         self.__MenuPPal.show()
         self.hide()
        
    def setControl(self,c):
        self.__control = c  

class VentanaDiagnostico(QDialog):
    def __init__(self, ppal = None): 

        super(VentanaDiagnostico, self).__init__(ppal)
        loadUi('VentanaDiagnostico.ui', self)
        self.__MenuPPal = ppal
        self.setUp()
        self.TI=[]

    def guardarTI(self,TI):
        self.TI=[TI]

    def verTI(self):
        return self.TI[0] 

    def eliminarTI(self):
        self.TI.clear()
    
    def visualizar(self):
        ti1=self.verTI()

        ti = self.__control.EditarPaciente(ti1)
        tie= self.__control.EditarExamenes(ti1)
        edad= ti[0][3]
        GR=self.__control.VerGlobulosRojos(edad,tie[0][1])
        GB=self.__control.VerGlobulosBlancos(edad,tie[0][2])
        PL =self.__control.VerPlaquetas(tie[0][3])
        HG=self.__control.VerHemoglobina(edad,tie[0][4])
        HM=self.__control.VerHematocrito(edad,tie[0][5])
        R=self.__control.VerReticulocitos(tie[0][6])

        self.label.setText(f"Ti del paciente: {ti[0][0]}\n Nombre del paciente: {ti[0][1]} \n Edad del paciente: {ti[0][3]} años \n Genero del paciente: {ti[0][5]}\n Estatura del paciente: {ti[0][2]}\n Peso del paciente: {ti[0][3]} Kg\n Niveles de gloubulos rojos: {GR} {tie[0][1]} 10**3/L \n Niveles de globulos blancos: {GB} {tie[0][2]} 10**3/ml \n Niveles de plaquetas: {PL} {tie[0][3]} 10**3\n Niveles de hemoglobina: {HG} {tie[0][4]} g/dl \n Niveles de hematocrito: {HM} {tie[0][5]} %\n Conteo de reticulocito: {R} {tie[0][6]} %")
    
    def setUp(self):
        self.salir.clicked.connect(self.exit)

    def exit(self):
         self.eliminarTI()
         self.__MenuPPal.show()
         self.hide()
        
    def setControl(self,c):
        self.__control = c 

class MyGraphCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(1,1,1)
        FigureCanvas.__init__(self, self.fig)

    def closeEvent(self, event): #----> este es con el fin de que las interfaces se puedan cerrar del 'close'
            self.close()
            self.parent().show()

    def graficaProme(self, datos):
        self.axes.clear() #se limpia los ejes
        self.axes.bar(datos[1], datos[0]) #Comando para histograma
        self.axes.set_xlabel('examen')
        self.axes.set_ylabel('promedio')
        self.axes.set_title(f'Promedio examenes entre {datos[2]}')
        self.draw()
    
    def graficarEquipos(self, datos):
        self.axes.clear()
        labels=datos[1]
        sizes=datos[0]
        colors = ['pink', 'blue', 'coral'] # se le asignan los colores para el equipo
        self.axes.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%') #gráfica de torta
        self.axes.set_title('Personas Registradas en el sistema') #se le asigna el nombre a la gráfica
        self.draw() #gracias a este se viasualiza
        
class VentanaEstadistica(QDialog):

    def __init__(self, ppal = None): 

        super().__init__(ppal)
        loadUi('VentanaEstadistica.ui', self)
        self.__MenuPPal = ppal
        self.setUp()

    def closeEvent(self, event):
            self.close()
            self.parent().show()
    def mostrar(self):
        a=0
        d=self.__control.calcularExam(0)
        self.label.setText(d)
    def setUp(self):
        
        self.layout = QVBoxLayout()
        self.graficoe.setLayout(self.layout)
        self.sc = MyGraphCanvas(self.graficoe, width=5, height=4, dpi=100) 
        self.layout.addWidget(self.sc)

        self.edad5.clicked.connect(self.edad_5)
        self.edad11.clicked.connect(self.edad_11)
        self.edad17.clicked.connect(self.edad_17)
        self.edades.clicked.connect(self.edad)
        self.boton_salir.clicked.connect(self.exit)

   #se hace la conexión entre la clase 'Gráficas' y 'MyGraphCanvas'
    def edad_5(self):
        a=1

        self.sc.graficaProme(self.__control.calcularExam(a)) 

    def edad_11(self):
        a=2
        self.sc.graficaProme(self.__control.calcularExam(a)) 

    def edad_17(self):
        a=3
        self.sc.graficaProme(self.__control.calcularExam(a))

    def edad(self):
        a=4
        self.sc.graficarEquipos(self.__control.calcularExam(a))

    def setControl(self,c):
        self.__control = c 

    def exit(self):
        self.__MenuPPal.show()
        self.hide()
