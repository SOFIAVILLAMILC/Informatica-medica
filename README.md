# Sistema de gestión de imagenes DICOM
<p align="justify">
Bienvenido al tutorial del sistema de gestión avanzada de imágenes python , donde exploraremos el proceso paso a paso para agregar estudios a pacientes, realizar consultas específicas, anonimizar estudios, convertir imágenes a formato nifti y eliminar estudios de manera eficiente.

## **Instrucciones:**
El tutorial se organiza en una serie de 4 pasos para implementar el sistema de gestión de inicio a fin:
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
  
class **Estudio** toma como atributos a la ruta del archivo dicom. Los métodos de esta clase son anonimzar archivos dicom de manera individual y en carpetas, convertir archivos dicom a formato NifTI y obtener información importante del estudio.
</p>

class **Paciente** toma como atributos el ID del paciente, su nombre y la lista de estudios que le corresponden. El método de esta clase es agregar estudios a la lista de cada paciente.
</p>

class **sistemaGestion** toma como atributo la lista de pacientes. Los metodos de esta clase son agregar pacientes a la lista, consultar la existencia del paciente, agregar, consultar y eliminar estudios de un paciente ademas de visualizar estudios en formato NifTI.
</p>


## **Paso 4 - Métodos de las clases** 
<p align="justify">
  
class **Estudio**

-  anonimizarDicom: Carga un archivo DICOM, elimina las etiquetas especificadas para anonimizar la información identificable, genera un nuevo UID para la instancia SOP y guarda el objeto DICOM anonimizado en un nuevo archivo en la ubicación especificada.

</p>  

-  anonimizarCarpeta: Recorre todos los archivos DICOM de una carpeta, los anonimiza uno por uno y guarda los archivos anonimizados en una ruta de salida específica.

</p>  

-  convertirNifti: Convierte todos los archivos DICOM a archivos NIfTI y guarda los resultados en una carpeta de salida específica.

</p>  

-  obtenerInfo: Devuelve un diccionario que contiene información detallada sobre el estudio, su ID, fecha, modalidad, descripción y dimensiones.

  
</p>

class **Paciente**

-  agregarEstudio: Añade un nuevo estudio a la lista de estudios de un paciente.
  
</p>

class **sistemaGestion**

-  agregarPaciente: Añade un nuevo paciente al sistema de gestión de pacientes si el ID del paciente no existe ya en el sistema.

 </p>   
 
-  consultarPaciente: Verifica si el paciente exista y devolver su información específica en el sistema de gestión.

 </p>   
 
-  agregarEstudio: Verifica si el paciente existe en el sistema, y si es así, agrega el estudio al paciente.

 </p>   
 
-  consultarEstudios: Verifica si el paciente tiene estudios asociados. Si el paciente tiene estudios recopila la información de cada estudio del paciente y la devuelve en forma de una lista de diccionarios llamada estudiosInfo, y si el paciente no los tiene entonces el método devuelve una lista vacía.

 </p>  

-  eliminarEstudio: Verifica si el paciente con el ID proporcionado existe en el sistema. Si el paciente existe, entonces se procede a buscar y eliminar el estudio específico dentro de la lista de estudios del paciente. Si el paciente no existe, se imprime un mensaje de error indicando que el paciente con el ID proporcionado no existe.
  
</p>  

-  visualizarEstudio: Permite la visualización de imágenes en formato NIfTI la cual puede realizarse en uno de tres modos: un solo plano, tres planos ortogonales o en mosaico. El plano se determina a partir de la entrada del usuario (input) y de las sentencias if que evalúan esa entrada.
  
</p>
<p align="justify">

## Ejemplo de la visualización de imágenes nifti

-  Visualización de estudio en modo mosaico:
![Mosaico](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/output.png)

</p>

-  Visualización de estudio en un solo plano:
![Un plano](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/imagen_2024-05-23_192340695.png)

</p>

-  Visualización de estudio en tres planos:
![Tres planos](https://github.com/SOFIAVILLAMILC/Informatica-medica/blob/main/tresplanos.png)
<p align="justify">

</p>


