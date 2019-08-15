# py-gunicorn-flask-prunus
> Created by Nicholas Ramsay

## Start server for Development
```bash
~ gunicorn --bind 0.0.0.0:5000 wsgi:app
```

## Start server for Production
```bash
~ gunicorn --bind 0.0.0.0:80 wsgi:app
```