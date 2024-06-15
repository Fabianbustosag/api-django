# Django API REST

## Comandos importantes

- `python manage.py migrate`
- `python manage.py makemigrations`
- `python manage.py inspectdb > ./api/models.py`

super user django-admin:

`python manage.py createsuperuser`

- user: admin
- pass: 12345

## Ahora

Crear el contenedor con la imagen

`docker-compose build`

Levantar el docker

`docker-compose up -d`

### Conexion a la DB (Docker)

Por comando dentro del contenedor

`psql -h localhost -p 5432 -U postgres -d postgres`

Por pgAdmin al (Docker)

- host: localhost
- port: 8001
- mainteined database: postgres
- user: postgres
- passsword: 12345

### Antes

Entrar al directorio del dockerfile

`cd /API`

Construir la imagen

`docker build -t api-rest .`

Ejecutar/Crear contenedor

`docker run -p 8000:8000 api-rest`

### DB Settings

TypeCount: se refiere a si es premium o no (se debe cambiar a TypeAccount)
