
 
from Modelo_ import sistema
from Vista_ import MenuPPal
import sys
from PyQt5.QtWidgets import QApplication
 
class Coordinador:
    
    def __init__(self, vista, sistema):
        self.__vista = vista 
        self.__sistema = sistema

    def validarUsuarioPac(self,TI):
        return self.__sistema.validarUsuarioPac(TI)

    def validarUsuarioMed(self, usu,cont ):
        return self.__sistema.validarUsuarioMed( usu,cont )  

    def validarPin(self,pin):
        return self.__sistema.validarPin(pin) 
    
    def IngresarUsuario(self,usu,cont):
        return self.__sistema.IngresarUsuario(usu,cont)
    
    def EliminarUsuario(self,usu):
        return self.__sistema.EliminarUsuario(usu)

    def IngresarPaciente(self, ti, nombre, estatura, peso, edad, genero):
        return self.__sistema.IngresarPaciente(ti, nombre, estatura, peso, edad, genero)

    def IngresarExamenes(self,TI,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,conteo_reticulocitos):
        return self.__sistema.IngresarExamenes(TI,globulos_rojos,globulos_blancos,plaquetas,hemoglobina,hematocrito,conteo_reticulocitos)
    
    def EditarPac(self, ti,nombre, estatura, peso, edad, genero):
        return self.__sistema.EditarPac(ti,nombre, estatura, peso, edad, genero)

    def EditarPaciente(self,ti):
        return  self.__sistema.EditarPaciente(ti)
    
    def EditarExam(self,ti,globulos_rojos,globulos_blancos,plaquetas, hematocrito,hemoglobina,conteo_reticulocitos):
        return self.__sistema.EditarExam(ti,globulos_rojos,globulos_blancos,plaquetas, hematocrito,hemoglobina,conteo_reticulocitos)
    
    def EditarExamenes(self,ti):
        return self.__sistema.EditarExamenes(ti)  

    def BorrarPaciente(self,ti):
        return self.__sistema.BorrarPaciente(ti)
    
    def BorrarExamen(self,ti):
        return self.__sistema.BorrarExamen(ti)
    
    def VerGlobulosRojos(self,edad,e):
        return self.__sistema.VerGlobulosRojos(edad,e)

    def VerGlobulosBlancos(self,edad,e):
        return self.__sistema.VerGlobulosBlancos(edad,e)

    def VerPlaquetas(self,e):
        return self.__sistema.VerPlaquetas(e)
    
    def VerHemoglobina(self,edad,e):
        return self.__sistema.VerHemoglobina(edad,e)
    
    def VerHematocrito(self,edad,e):
        return self.__sistema.VerHematocrito(edad,e)
    
    def VerReticulocitos(self,e):
        return self.__sistema.VerReticulocitos(e)

    def calcularExam(self,senal):
        return self.__sistema.calcularExam(senal)
        
class Principal(object):
    def __init__(self):
      self.app = QApplication(sys.argv)
      self.sistema = sistema()
      self.vista = MenuPPal()
      self.control = Coordinador(self.vista,self.sistema)
      self.vista.setControl(self.control) 

    def main(self):
        self.vista.show()
        sys.exit(self.app.exec_())  

if __name__ == '__main__':
    p = Principal()
    p.main()