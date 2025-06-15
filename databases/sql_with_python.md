# SQL with Python

## 12. SQL and python

untill now we have been using Dbeaver to interact with the database (as the client)
from now on we will be using python to interact with the database (as the client)
the framework we will be using is called SQLAlchemy
this framework is a python library that provides a way to interact with databases using python

first we need to install the SQLAlchemy library and psycopg2 library (psycopg2 is a library that allows us to connect to the database)
```bash
pip install sqlalchemy psycopg2
```

first step with sqlalchemy on python
```python
from sqlalchemy import create_engine

USERNAME = 'myuser'
PASSWORD = 'mypassword'
HOST = 'localhost'
PORT = '5432'
DATABASE_NAME = 'college'

# URI is the Uniform Resource Identifier (the address of the database)
URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}'
# create the engine (will allow us to connect to the database)
engine = create_engine(URI)
```
## to run a query we need to create connection

```python
connection = engine.connect()


```

