# Amo-a-los-perros

## Configuracion para desarrolladores

1) Cuenta en heroku app
2) Instalar toolbet en consola
3) correr el comando `heroku login` para que se heroku habilite la consola para tirar comandos.
4) bajarse el repo de github si ya no lo tienen.
5) agregar el remoto de heroku para deployar: heroku git:remote -a amoalosperros
6) con un simple `git push heroku master` se deploya a produccion, o sea a --> https://amoalosperros.herokuapp.com
7) para correr la app en local se debe hacer `pip install -r requirements.txt` por unica vez y luego cuando se quiera arrancar el servidor local `heroku local web -p 8000` para correrlo en el puerto 8000
8) recomiendo instalar nginx, habilitar un virtual host en `/etc/nginx/sites-enabled/amoalosperros` y crear el hosts en `/etc/hosts` como lo hicimos en el taller. o sea que cuando se le pegue a amoalosperros.com redireccione a 127.0.0.1:

#### Configuracion para virtual host
```
server {
    listen 80;
    server_name amoalosperros.com;

    location / {
        proxy_pass       http://127.0.0.1:8000;
        proxy_set_header Host      $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

```

### Condiciones
Para el paso 5, tengo que agregarlos como partes del proyecto imagino para que puedan hacer push, etc. Pidanmelo por mail.

### Cualquier consulta me escriben por mail. ;)