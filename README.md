# Steps to reproduce ```ORA-01461: can bind a LONG value only for insert into a LONG column```

1. ```pip install -r requirements```
1. update *DATABASES* in settings.py
1. ```python manage.py migrate```
1. ```python manage.py loaddata dumped.json```

Tested on Oracle Database 11g Enterprise Edition Release 11.2.0.1.0