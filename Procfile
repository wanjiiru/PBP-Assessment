web: gunicorn wsgi:app -c settings.py --log-file -
release: python manage.py db upgrade
