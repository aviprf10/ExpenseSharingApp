# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    mobile_number = db.Column(db.String)
    balances = db.relationship('Balance', back_populates='user')

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payer_id = db.Column(db.String, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    expense_type = db.Column(db.String)
    description = db.Column(db.String)
    participants = db.relationship('Participant', back_populates='expense')

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id'))
    share = db.Column(db.Float)

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    balance = db.Column(db.Float)
    user = db.relationship('User', back_populates='balances')
