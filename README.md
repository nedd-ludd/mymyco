# mymyco
Growing and cultivation management software for Mycology
git clone
pipenv install or pipenv install --dev
note dev to play around
pipenv shell


create .env file containing:
```
# PostgreSQL Database Settings
POSTGRES_NAME=mymyco
POSTGRES_HOST=localhost
POSTGRES_PORT=****?
POSTGRES_USER=******?
POSTGRES_PASSWORD=****************?
```



python manage.py migrate
python manage.py createsuperuser - is this needed?
python manage.py runserver

