# estates_backend


###Introducción


Puede probar el proyecto en: []()

*****


### Características

* Registrarse
* Iniciar sesión
* Crea un predio propio
* Ver todos los predios que ha creado
* Ver todos los predios por usuario del sistema
* Editar su información del perfil
* Cerrar sesión
* Para añadir predios debe estar autenticado.


### Variables De Entorno
* Archivo de variables de entorno: .env
```
#Django
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
SECRET_KEY=

ALLOWED_HOSTS=
```

### Desarrollo
* Construye y lanza el proyecto en un servidor local y de desarrollo.
``` bash
make build
make up
make migrate
make makemessages
make compilemessages
```

* Si necesitas un super usuario
```bash
make superuser
```


### Producción
* Construye y lanza el proyecto para producción.
``` bash
make prod-buil
make prod-run
make prod-migrate
make prod-makemessages
make prod-compilemessages
```

### Makefile

Los comandos de producción son los mismos que los de desarrollo, pero es necesario poner "prod-" al principio.
* Crear y correr migraciones
``` bash
make migrate
```

* Correr collectstatic
``` bash
make statics
```

* Crear super usuario
``` bash
make superuser
```

* Crear una app
``` bash
make app APP_NAME=my_app
```

* Crear mensajes para la internacionalización
``` bash
make makemessages
```

* Compilar mensajes para la internacionalización
``` bash
make compilemessages
```