# Deusto11.Nexus
The new Nexus web site.

# Información básica
El trabajo se basa en la aplicación (deusto11components), el proyecto(deusto11nexus)  y los servicios (deusto11services) como funcionalidad.
El proyecto tiene tres clases como vemos que son Equipo, Ticket y empleado con sus respectivos atributos.
Hemos definido una relación de un empleado puede tene un ticket y un ticket puede tener un equipo.
Antes de empezar la aplicación tenemos un login y register de empleado. En la aplicación se ha creado una vista dedicada a los logins.
Si abrimos el UML:

-Tenemos el base.html que es de donde heredan todas las vistas

-Tenemos index que tiene login con el que nos logearemos y registrarse con el que crearemos un nuevo empleado

-EmployerPortal ahí tendremos los datos del empleado y tendremos un botón por si queremos actualizarlo

También tenemos los tickets creados y podemos tener la opción de actualizar y eliminarlo

Esta la opción de crear un nuevo ticket o equipo:

-Tenemos la vista de employerRegistry que lo utilizaremos para añadir un nuevo empleado con cada de uno de sus atributos

-Tenemos también la vista de ticketRegistry en el que crearemos un nuevo ticket con todos sus atributos o actualizaremos la máquina

-La ultima vista es machine registry con la que meteremos nuevos registros

-Tenemos una vista de actualizar por cada una de las clases por si queremos cambiar cada uno de los objetos que hemos creado

-Tenemos también una vista creada de vlog con la que accedemos por si queremos documentarnos de nuestra aplicación


Por cada vista hay un html creado en la carpeta de templates que heredan todos de base 
En base hereda de la carpeta de static que hay está dentro todo el css del trabajo

Para los botones hemos creado lo primero todas las urls de login, registrar y actualizar y le hemos pegado la url
Para trabajar en cada una de las vistas bastaba con poner la direcciónip/nexus.com/ y lo que quisieramos buscar

Como ya se ha mencionado antes para acceder en la aplicación es ladirecciónip/nexus.com/

En vez de crear una Delete view y hacer más htmls hemos creado un vista de delete con métodos get y post

En deustoservices todavía no hay nada pero estarán los servicios de la aplicación.

Cabe destacar que hemos trabajado en el repositorio subiendo los cambios haciendo commits y pull request en los que nos evitaba que hubiera conflictos y que la aplicación diera errores 

En los models están creados todos los fields de los atributos de las clases que se ha mencionado antes y se han puesto los str para que podamos ver los atributos del objeto creado

# Funcionalidad Deusto11_Nexus_services
El paquete que hereda funcionalidades nexus_componenets (como ya hemos conmentado, la aplicación), tiene como objetivo 3 clases diferenciadas. auth.py se encarga de hacer asegurarse que el usuario existe concidiendo usuario y contraseña a partir de un modelo que se ha creado. La calse de los log simplemente es para obtener por el terminal que la funcionalidad es correcta. Se podía haber utilizado los logs de djgango pero la configuración se consideró trabajo innecesario.

Por último la clase viewsManagerService probe a las views de métodos como la construcción context.
