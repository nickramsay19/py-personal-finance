# py-personal-finance
> Created by Nicholas Ramsay

## Start server for Development
``` bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
* Runs server without gunicorn
* Runs server on port 5000
* Runs flask in development mode

## Start server for Production
``` bash
gunicorn --bind 0.0.0.0:80 wsgi:app
```
* Runs server on port 80 (default HTTP port)

## Todo
### Client
* Remove layout from login and create an independent page for logging in, ideally in a modal.