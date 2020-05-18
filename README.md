# Deusto11.Nexus
Nexus es una aplicación de mantenimiento de incidencias. Provee a los empleados la correcta información por medio de tickets asegurarse del mantenimiento de los equipos.

## Desarrollo
El desarrollo del proyeto se basa en la utilización de un sistema de tareas que proporciona [github](https://github.com/orgs/Grupo-Proyecto-Ingenieria-Web/projects/1) a nivel de organización. También se ha pensado de utilización de una tabla compartida en google drive. El sistema de trabajo es simple, se define una tarea y el desarrollador crea una rama a partir de la rama con las modificaciones más recientes (máster). 

Una vez que ha acabado una tarea o parte de una tarea se hace un pull request.

## Organización de Nexus
Nexus está formada por tres partes diferenciadas. El proyecto [deusto11_nexus](https://github.com/Grupo-Proyecto-Ingenieria-Web/Deusto11.Nexus/tree/master/deusto11_nexus/deusto11_nexus) utiliza una aplicación [deusto11_nexus_components](https://github.com/Grupo-Proyecto-Ingenieria-Web/Deusto11.Nexus/tree/master/deusto11_nexus/deusto11_nexus_components) encargada de de proveer la lógica de negocio y la lógica de presentación. También para proveer de manera lógica métodos que varias clases utilizan en la aplicación, se ha creado un módulo [deusto11_nexus_services](https://github.com/Grupo-Proyecto-Ingenieria-Web/Deusto11.Nexus/tree/master/deusto11_nexus/deusto11_nexus_services).

### Deusto11_nexus
Como se ha comentado, es el proyecto de la aplicación, la bese sobre la que inicia. Aquí se han agregado configuraciones adicionales para añadir la aplicación.

Añadiendo `path('nexus.com/', include('deusto11_nexus_components.urls'))` se define la direccón de la aplicación que el proyecto va a utilizar. También se añaden configuraciones para los archivos estáticos dentro de la aplicación:
```
STATIC_URL = '/static/'
STATICFILES_DIR = [os.path.join(BASE_DIR, 'static')] # definir carpeta de estaticos
```
### Deusto11_nexus_components
Es la aplicación que provee las vistas y la lógica de negocio que interactúa con la base de datos de django. También se definen los modelos con los que django de forma interna utiliza para crear las tablas y los formularios a la hora de obtener datos.

¿Cómo funciona la aplicación?

### Deusto11_nexus_services
Es el paquete que provee de los métodos como logs, autenticación y métodos construcción de contextos.
