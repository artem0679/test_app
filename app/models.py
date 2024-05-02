import os
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask import url_for, current_app
from app import db
import markdown
import bleach
from sqlalchemy.dialects.mysql import YEAR


class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    # Название роли
    name = db.Column(db.String(100), nullable=False)
    # Описание роли
    description = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return '<Role %r>' % self.name


class Products1(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    # Название формы обучения (дневная/вечерняя/заочная)
    prod_name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password1 = db.Column(db.String(200), nullable=False)
    count_of_prod = db.Column(db.Integer, nullable=False)
    # ФИО

    def check_password(self, password) -> bool:
        return (self.password1 == password)

    @property
    def full_name(self) -> str:
        return ' '.join([self.last_name,
                         self.first_name,
                         self.middle_name or ''])

    def is_admin(self):
        return self.role_id == current_app.config['ADMIN_ROLE_ID']

    def is_student(self):
        return self.role_id == current_app.config['STUDENT_ROLE_ID']

    def __repr__(self):
        return '<User %r>' % self.login


class Reporting_form(db.Model):
    __tablename__ = "reporting_forms"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100))



