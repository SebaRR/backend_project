# Backend_project
Proyecto de prueba que consiste en dos tareas, para la tarea 1 se usa la libreria requests para obtener información de la página web, luego son almacenadas y 
mostradas en una pagina hecha con bootstrap y para la tarea 2 se intento utilizar Selenium WebDriver (aunque era mi primera vez utilizando, logre entender el funcionamiento, 
mas no completar la tarea, con mas tiempo de estudio estoy seguro que lo hubiese logrado.
## Instalación 
Se utiliza el framework Django 4, las librerias psycopg2-binary (para el uso de DB PostgreSQL), requests y selenium.
## Uso
Al ingresar al index del trabajo se presentan tres botones, "Tarea 1" (para acceder a la vista de la tarea 1), "Tarea 2" (para acceder a la vista de la tarea 2) y "Panel de Administrador" (para 
acceder a la vista del panel de administrador).
## Supuestos 
* Tarea 1: Se extraen los veinte (20) primeros datos para no sobrecargar el trabajo con la base de datos. Cada vez que se accede a la vista de tarea 1, se realiza el guardado de los datos, si estos existen solo
se imprime el error del form correspondiente. Para hacer el ingreso al panel de administrador debe hacerse a traves de un superuser
* Tarea 2: Se crea el modelo a partir de lo que se observa al aplicar el filtro en la pagina web.
* Bootstrap: Primera vez utilizando bootstrap, teniendo mas tiempo podria realizar un mejor trabajo, al igual que con selenium.
* Migraciones hechas, solo es necesario hacer la migracion.
