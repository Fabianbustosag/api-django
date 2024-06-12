# Django API REST

## Ahora

Crear el contenedor con la imagen

`docker-compose build`

Levantar el docker

`docker-compose up -d`

### Conexion a la DB (Docker)

Por comando dentro del contenedor

`psql -h localhost -p 5432 -U postgres -d postgres`

Por pgAdmin

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
