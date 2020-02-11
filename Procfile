web: gunicorn wsgi:app -c settings.py --log-file -
flask db migrate
flask db upgrade
