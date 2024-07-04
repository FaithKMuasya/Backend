from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime


db = SQLAlchemy()

class Income(db.Model):
    __tablename__ = 'income'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def to_dict(self):
            return {
                'id': self.id,
                'description': self.description,
                'amount': self.amount,
                'date': self.date.strftime('%Y-%m-%d'),
                'user_id': self.user_id
            }

class Savings(db.Model):
        __tablename__ = 'savings'

        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(100), nullable=False, unique=True)
        amount = db.Column(db.Float, nullable=False)
        date = db.Column(db.Date, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
        def to_dict(self):
                return {
                    'id': self.id,
                    'description': self.description,
                    'amount': self.amount,
                    'date': self.date.strftime('%Y-%m-%d'),
                    'user_id': self.user_id,
                    'category_id': self.category_id
                }


class Expenses(db.Model):
        __tablename__ = 'expenses'

        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(100), nullable=False, unique=True)
        amount = db.Column(db.Float, nullable=False)
        date = db.Column(db.Date, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
        def to_dict(self):
                return {
                    'id': self.id,
                    'description': self.description,
                    'amount': self.amount,
                    'date': self.date.strftime('%Y-%m-%d'),
                    'user_id': self.user_id,
                    'category_id': self.category_id
                }


class Categories(db.Model):
        __tablename__ = 'category'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False, unique=True)
        expenses = db.relationship('Expenses', backref='category', lazy=True)
        savings = db.relationship('Savings', backref='category', lazy=True)
        def to_dict(self):
                return {
                    'id': self.id,
                    'name': self.name
                }

class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), nullable=False, unique=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(50), nullable=False, unique=True)
        incomes = db.relationship('Income', backref='user', lazy=True)
        savings = db.relationship('Savings', backref='user', lazy=True)
        expenses = db.relationship('Expenses', backref='user', lazy=True)
        def to_dict(self):
                return {
                        'id': self.id,
                        'username': self.username,
                        'email': self.email,
                        'password': self.password
                }

    