web: gunicorn addiction_trial.wsgi.application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py migrate