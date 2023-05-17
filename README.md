# BaseDeProyectoDBP
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

# Objetivos principales / Misión / Visión.

Objetivos principales: Como proyecto buscamos integrar todos los principios de la contabilidad en un sistema para hacer más eficiente el proceso de inventario

Mision: Nuestra misión, o alcance, es ser una plataforma user-friendly, para que personas sin un conocimiento previo contable puedan usar de una manera sencilla la página.

Visión: Tenemos como visión seguir mejorando el proyecto pero de la mano de nuestros products owners. En otras palabras, personalizar/adaptar el sistema según las necesidades que requiera el contexto. 

# Nombre del script a ejecutar para iniciar la base de datos con datos:
No tenemos un ejecutable como tal; sin embargo, contamos con un script que es activable con un botón dentro del programa
Registrarte como employee -> Login como employee -> boton "make a purchase" --> presionar el primer boton (el cual genera 8 productos pre-definidos con constructores) --> puedes modificar la cantidad de un producto (opcional) --> Submit
OJO: Crear database 'tienda'

http://localhost:5000/





