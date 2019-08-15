# py-gunicorn-flask-prunus
> Created by Nicholas Ramsay

## Start server for Development
```bash
~ gunicorn --bind 0.0.0.0:5000 wsgi:app
```
* Runs server without gunicorn
* Runs server on port 5000
* Runs flask in development mode

## Start server for Production
```bash
~ gunicorn --certfile=keys/server.crt --keyfile=keys/server.key --bind 0.0.0.0:80 wsgi:app
```
* Runs server on port 80 (default HTTP port)
* Runs server with SSL support to listen for HTTPS