# Sistema de gestión de imagenes DICOM
<p align="justify">
Bienvenido al tutorial del sistema de gestión avanzada de imágenes python , donde exploraremos el proceso paso a paso para agregar estudios a pacientes, realizar consultas específicas, anonimizar estudios, convertir imágenes a formato nifti y eliminar estudios de manera eficiente.

## **Instrucciones:**
El tutorial se organiza en una serie de x pasos para implementar el sistema de gestión de inicio a fin:
## **Paso 0 - Definición del Problema**
<p align="justify">
En el ámbito de la investigación clínica, la gestión de imágenes médicas y su correspondiente metadata es fundamental para garantizar tanto la integridad del proceso investigativo como la privacidad de los pacientes. Las imágenes DICOM, que contienen datos detallados tanto clínicos como personales, requieren un manejo cuidadoso para evitar la divulgación de información identificable. 
<p align="justify">
Este proyecto tiene como objetivo desarrollar un sistema en Python que no solo gestione y anonimice estas imágenes, sino que también proporcione una estructura organizativa que identifique y catalogue imágenes de acuerdo a los pacientes y sus respectivos estudios médicos.
</p>

## **Paso 1 - Configurar el entorno de trabajo**

Las librerías utilizadas son:

-  pydicom, numpy, os, dicom2nifti, nilearn, nibabel.

## **Paso 2 - Diagrama de clases**


![Diagrama de clases desarrollado](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/Blank%20Diagram.png)
Se establece una relación de dependencia de la clase sistemaGestion hacia las clases Paciente y Estudio.
<p align="justify">
</p>

## **Paso 3 - Diseño de clases**

<p align="justify">
class "Estudio" toma como atributos a la ruta del archivo dicom. Los métodos de esta clase son anonimzar archivos dicom de manera individual y en carpetas, convertir archivos dicom a formato nifti y obtener información importante del estudio.
</p>
class "Paciente" toma como atributos el ID del paciente, su nombre y la lista de estudios que le corresponden. El método de esta clase es agregar estudios a la lista de cada paciente.
</p>

class "sistemaGestion" toma como atributo la lista de pacientes. Los metodos de esta clase son agregar pacientes a la lista, consultar la existencia del paciente, agregar, consultar y eliminar estudios de un paciente ademas de visualizar estudios en formato nifti.
</p>


## **Paso 4 - Pruebas de funcionalidad** 
**Visualizar estudio**

-  Visualización de estudio en modo mosaico:
![Mosaico](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/output.png)

</p>

-  Visualización de estudio en un solo plano:
![Un plano](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/unsoloplano.png)

</p>

-  Visualización de estudio en tres planos:
![Tres planos](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/tresplanos.png)
<p align="justify">

</p>


