import os

SECRET_KEY = "f4a4610d-366b-40f0-bc2c-6df1c6deb766"

params = {
    "username": "root",
    "password": "root",
    "db_name": "academic_performance1",
    "db_url": "localhost",
}

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{params.get("username")}:{params.get("password")}@{params.get("db_url")}/{params.get("db_name")}'

ADMIN_ROLE_ID = 1
MODERATOR_ROLE_ID = 2
STUDENT_ROLE_ID = 3
