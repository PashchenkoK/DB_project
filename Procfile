web: gunicorn root.main:app --log-file -
web: flask db upgrade; flask translate compile; gunicorn microblog:app