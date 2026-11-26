# Registro Personal de Gastos | versión 2



## Descripción:

Aplicación de consola que registra y administra mediante una base de datos relacional SQLite todos los gastos personales que se agreguen. La aplicación permite agregar, ver, modificar y eliminar los gastos registrados. A su vez, permite visualizar la suma total de los gastos, agruparlos por categorías, calcular gastos mensuales y filtrar gastos según fecha, descripción o categoría.


## Objetivo:

El proyecto tiene como objetivo implementar conocimientos del lenguaje Python con el fin de fortalecer el aprendizaje. El proyecto evolucionará en diferentes versiones, siendo ésta la segunda versión. 



## Funcionalidades:
 
La aplicación ofrece las siguientes funcionalidades:

  - Menú para acceder a las diferentes opciones.
  - Función para agregar nuevos gastos.
  - Función para ver los gastos registrados. 
  - Función para filtrar los gastos registrados y submenú para filtrarlos según fecha, descripción o categoría.
  - Función para modificar gastos registrados. 
  - Función para eliminar gastos registrados. 
  - Función para sumar el importe de todos los gastos registrados.
  - Función para sumar el importe de los gastos registrados en un mes.
  - Función para agrupar los gastos registrados según categorías.


## Tecnologías empleadas:

- **Python 3.11.2**
- **SQLite3**



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



# Funcionamiento:

- La aplicación está pensada para que al ejecutar el proyecto, la consola muestre el menú con las opciónes disponibles.

- Todos los gastos que se agreguen quedarán almacenados en la base de datos.

- La aplicación validará las entradas del usuario para que no se ingresen datos no válidos como texto en campos numéricos o números en campos de texto. 




## Limitaciones:

Esta version no permite:

- Visualizarse en un navegador web.

- Exportar datos a un archivo Excel.




## Mejoras y próximas versiones:

La próxima versión incorporará las siguientes funcionalidades: 

- Obtener estadísticas de gastos y visualizar las categorías de mayor y menor consumo.

- Exportar los gastos registrados a un archivo Excel o PDF.

- Crear una lista de categorías predefinidas tales como impuestos, salud, etc. y permitir al usuario crear las propias. 
