# Registro Personal de Gastos


## Descripción:

Aplicación de consola que registra y administa en un archivo de tipo txt, todos los gastos personales que se agreguen. La aplicación permite agregar, ver, modificar y eliminar los gastos registrados. A su vez, permite visualizar la suma total de los gastos y agruparlos por categorías. 

## Objetivo:

El proyecto tiene como objetivo implementar conocimientos del lenguaje Python con el fin de fortalecer el aprendizaje. El proyecto evolucionará en diferentes versiones, siendo ésta la versión inicial. 


## Funcionalidades:
 
La aplicación cuenta con
  - Menú para acceder a las diferentes opciones.
  - Función para ver los gastos registrados. 
  - Función para agregar nuevos gastos. 
  - Función para modificar gastos registrados. 
  - Función para eliminar gastos registrados. 
  - Función para sumar el importe de los gastos registrados.
  - Función para agrupar los gastos registrados según categorías.

## Tecnologías empleadas:

- **Python 3.11.2**
- **Archivo de texto para el almacenamiento de los datos**


## Requisitos:

Antes de comenzar es necesario tener instalado [Python](https://www.python.org/downloads/) 3.8 o superior (desarrollado originalmente en Python 3.11).

## Instalación:

- Descargar como zip o clonar el repositorio:

```bash
git clone https://github.com/SaraEOlivera/Personal-Expense-Tracker
```

- Ejecutar el proyecto:

```bash
python main.py
```

# Functionamiento:

- La aplicación está pensada para que al ejecutar el proyecto, la consola muestre los gastos registrados, si los hubiere, y el menú con las opciónes disponibles.

- Todos los gastos que se agreguen quedarán almacenados en el archivo gastos.txt.

- La aplicación validará las entradas del usuario para que no se ingresen datos no válidos tales como texto en el campo de gastos. 


## Limitaciones:

Esta version no permite:

- Clasificar gastos por fechas.

- Modificar detalles o categorías de los gastos registrados.

- Ninguna otra funcionalidad que no esté implementada en el programa.


## Mejoras y próximas versiones:

Al ser ésta la versión inicial, la próxima versión permitirá almacenar los registros de gastos en una base de datos SQL y permitirá, además, agrupar gastos según las fechas de ingreso. 
