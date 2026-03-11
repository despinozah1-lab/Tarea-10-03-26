# Árbol Binario de Búsqueda en Python

## Descripción

Este proyecto implementa un Árbol Binario de Búsqueda (ABB) en Python con una interfaz de línea de comandos (CLI).
El programa permite insertar, buscar y eliminar números dentro del árbol, así como cargar datos desde archivos de texto.

Además, el programa genera automáticamente una representación visual del árbol utilizando Graphviz.

## Requisitos

Para ejecutar el programa es necesario tener instalado:

* Python 3
* Graphviz
* Librería graphviz para Python

Instalar la librería de Python con el siguiente comando:

pip install graphviz

También es necesario instalar Graphviz en el sistema operativo.
Puede descargarse desde:

https://graphviz.org/download/

## Archivos de ejemplo

El repositorio incluye varios archivos .txt con números que pueden utilizarse para cargar datos al árbol:

* numeros_basicos.txt
* numeros_grandes.txt
* numeros_desbalanceados.txt
* numeros_random.txt
* prueba.txt

Cada archivo contiene un número por línea, el cual será insertado en el árbol binario de búsqueda.

## Cómo ejecutar el programa

1. Abrir una terminal o CMD.
2. Navegar a la carpeta del proyecto.
3. Ejecutar el programa con el siguiente comando:

py -3 arbol_binario.py

También puede ejecutarse con:

python arbol_binario.py

## Uso del programa

Al iniciar el programa se mostrará un menú interactivo con las siguientes opciones:

1. Insertar número
2. Buscar número
3. Eliminar número
4. Cargar desde archivo
5. Visualizar árbol
6. Salir

Para cargar números desde un archivo, seleccionar la opción correspondiente e ingresar la ruta del archivo .txt.

## Visualización del árbol

El programa genera automáticamente la visualización del árbol utilizando Graphviz.

Cuando se selecciona la opción de visualizar el árbol, el programa crea una imagen del árbol binario y la abre automáticamente.

Las imágenes generadas no se incluyen en el repositorio ya que son creadas dinámicamente por el programa durante su ejecución.

## Autor

Proyecto desarrollado como práctica académica para la implementación de estructuras de datos en Python.
