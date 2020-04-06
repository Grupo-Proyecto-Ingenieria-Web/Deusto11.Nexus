# WORKON

# workon [nombre_entorno]

# deactivate

# rmvirtualenv [nombre_entorno]

# mkvirtualenv [nombre_entorno]

# Para crear un entorno y projecto a la vez, asilado en la capeta prefijada project_home
# mkproject [nombre_projecto]

# ---------------------------------------------------------------------------------------------------------

# django-admin startproject [nombre_projecto_django] (esto dentro del entorno ya creado con projecto de entorno)

# ---------------------------------------------------------------------------------------------------------

# Iniciar nueva app
# python manage.py startapp [nombre app]

# Para iniciar instancia
# python manage.py runserver (obviamente dentro del directorio del proyecto, HAY QUE ESTAR COPMO ADMINISTRADOR)

# Para crear los modelos definidos
# python manage.py makemigrations [nombre_app ]

# Una vez creaas se migran --> en la clase initial de la carpeta migrate se puede ver
# python manage.py migrate

# Para comunicarse con la consola python
# python manage.py shell

# python manage.py createsuperuser

# --------------------------------------------------------------------------------------------------------------

# from appPruebaDos.models import Duracion, Genero, Articulo
# duracion = Duracion(nombre = "Duracion corta", duracionMin = 125)
# duracion.save()
# duracion.id
# Duracion.objects.all()
# Para hacer un select más complejo
# Duracion.objects.filter(nombre__contains='Duracion corta').count()