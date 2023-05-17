﻿# BaseDeProyectoDBP
#IMPORTANTE
Nuestro proyecto está dentro de un paquete "app", para iniciarlizarlo en un sistema operativo windowns sigue los siguientes pasos:

1. Clonar el repositorio
2. Creen un ambiente virtual, el nombre preferentemente debe ser "env"
3. Instalar las librerias AMBIENTE VIRTUAL "pip install -r requirements.txt"
4. Poner una serie de comandos: 
    $env:FLASK_APP = "app"  //Acá estas asignando la variable de entorno = "app", el paquete app ejecutará el archivo __init__.py.
    $env:FLASK_DEBUG = 1    //Pones el modo debug = 1, osea en true
    flask run               // Finalmente ponen flask run y el programa debe correr en el puerto http://localhost:5000

#INTEGRANTES
-Aldo Gianfranco
-Alejandro Marcelo
-Esteban Sulca Infante

#DESCRIPCION
Software de asístencia para administrativos empresariales: permitirá controlar y registrar el inventario y las ventas; así como también generará herramientas contables (estado de resultados)
