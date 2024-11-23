Programa de Análisis de ADN
Este programa permite analizar secuencias de ADN para detectar mutaciones, realizar mutaciones en el ADN y sanarlo si es necesario. Las mutaciones pueden ser generadas por radiación (horizontal o vertical) o por un virus (diagonal). El programa tambien permite detectar si una secuencia de ADN contiene mutaciones y sanarla automáticamente si es necesario.

Participantes del Grupo
Adriel Ezequias Isgro
Juan Pablo Gomez
Leandro Benaiges
Lucas Ledesma

Cómo se ejecuta nuestro programa:

El programa presenta un menú con varias opciones para interactuar con el ADN:

Detectar mutaciones: El programa le dirá si su ADN tiene mutaciones .

Mutar el ADN: SE puede agregar mutaciones en el ADN de dos formas:

Radiación: Cambia el ADN en forma horizontal o vertical.

Virus: Agrega mutaciones en forma diagonal.

Sanar el ADN: Si tu ADN tiene mutaciones, el programa intentará sanarlo, creando una nueva secuencia de ADN sin errores.

A continuación, se muestra un ejemplo de cómo ejecutar el programa:

El usuario debe ingresar una matriz de ADN, que consiste en 6 filas y 6 columnas de bases nitrogenadas (A, T, C, G).

Ejemplo de matriz de entrada:

Copiar código
ATGCAT
TACGGT
GGCATA
TCGGCT
ATCGAT
GGCTAT
El programa detectará si hay mutaciones en la secuencia, mostrando este mensaje:

Resultado: Mutante

Luego, el usuario puede optar por mutar el ADN, por ejemplo, usando la opción de "Mutación por Virus (Diagonal)", eligiendo una dirección como hacia abajo-derecha (↘).

El programa realizará la mutación en la matriz y la mostrará:

Nuevo ADN:

ATGCAT
TACGGT
GGCATA
TCGGCT
ATCGAT
GGTTAT

Finalmente, el usuario puede optar por "Sanar el ADN", y el programa intentará restaurar el ADN a una forma sin mutaciones.

Ejemplo de salida:

ADN sanado:

ATGCAT
TACGGT
GGCATA
TCGGCT
ATCGAT
GGCTAT

Estructura del código

             Clases:

Detector: Esta clase se encarga de detectar mutaciones en las secuencias de ADN.
Mutador: Clase base para realizar mutaciones en el ADN.
Radiación: Subclase de Mutador para mutaciones horizontales o verticales.
Virus: Subclase de Mutador para mutaciones diagonales.
Sanador: Clase para sanación del ADN, que genera nuevas secuencias de ADN sin mutaciones.

            Funciones principales:

validar_posicion: Valida si una posición está dentro de los límites de la matriz de ADN.
solicitar_posicion: Solicita al usuario una posición válida para realizar una mutación.
solicitar_matriz: Solicita al usuario que ingrese la matriz de ADN.
mostrar_matriz: Muestra la matriz de ADN actual.