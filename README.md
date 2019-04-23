# Django_Vue_Chart
Python - https://www.python.org/downloads/  
PostgreSQL - https://www.postgresql.org/download/

### Install dependencies:
```Python 
pip install -r require.txt
```

### Starting backend:
```Python
cd django_project
python manage.py runserver
```

### Database configuration
#### Default
Name: maindb
Port: 5432

This can be changed in settings.py

#### PostgreSQL post-install database creation
```
cd django_project
python manage.py migrate --run-syncdb
```

