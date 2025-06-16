import os

USERNAME = 'myuser'
PASSWORD = 'mypassword'
DB_LOCALHOST = 'localhost'
DB_CONTAINER_HOST = 'college-db-container'
DB_PORT = '5432'
DATABASE_NAME = 'postgres'
TABLE_NAME = 'students'
DOCKER_ENV = os.getenv('DOCKER_ENV', 'false')

if DOCKER_ENV:
    DB_URI = f'postgresql://{USERNAME}:{PASSWORD}@{DB_CONTAINER_HOST}:{DB_PORT}/{DATABASE_NAME}'
else:
    DB_URI = f'postgresql://{USERNAME}:{PASSWORD}@{DB_LOCALHOST}:{DB_PORT}/{DATABASE_NAME}'







