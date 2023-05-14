#Imports
from flask import (
    Flask, 
    request,
    jsonify,
    render_template
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys
from datetime import datetime
import uuid

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/accountech'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)
    role = db.Column(db.String(80), nullable = False)
    sales = db.relationship('Sale', backref='employee', lazy=True)
    buys = db.relationship('Buy', backref='employee', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, firstname, lastname, role):
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        self.is_active = True
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Employee %r %r>' % (self.firstname, self.lastname)
    
    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'is_active': self.is_active,
            'role': self.role,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
        }
    
class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    object = db.Column(db.String(80), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    employee_id = db.Column(db.String(36), db.ForeignKey('employees.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))
    
    def __init__(self, object, quantity, amount):
        self.object = object
        self.quantity = quantity
        self.amount = amount
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Sale %r %r for %r>' % (self.quantity, self.object, self.amount)
    
    def serialize(self):
        return {
            'id': self.id,
            'object': self.object,
            'quantity': self.quantity,
            'amount': self.amount,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
        }
    
class Buy(db.Model):
    __tablename__ = 'buys'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), server_default=db.text("uuid_generate_v4()"))
    object = db.Column(db.String(80), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    employee_id = db.Column(db.String(36), db.ForeignKey('employees.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()"))
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()"))

    def __init__(self, object, amount, quantity):
        self.object = object
        self.quantity = quantity
        self.amount = amount
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Buy %r %r for %r>' % (self.quantity, self.object, self.amount)
    
    def serialize(self):
        return {
            'id': self.id,
            'object': self.object,
            'quantity': self.quantity,
            'amount': self.amount,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
        }
    
class Inventory(db.Model):
    __tablename__ = 'inventoy'
    object = db.Column(db.String(80), primary_key = True, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()")) #delete
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()")) #actualiced_at

    def __init__(self, object, amount, quantity):
        self.object = object
        self.quantity = quantity
        self.amount = amount
        self.created_at = datetime.utcnow()

    def serialize(self):
        return {
            'object': self.object,
            'quantity': self.quantity,
            'amount': self.amount,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
        }

class Expense(db.Model):
    __tablename__ = 'expenses'
    type = db.Column(db.String(80), primary_key = True, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=db.text("now()")) #incurent_at
    modified_at = db.Column(db.DateTime(timezone=True), nullable=True, server_default=db.text("now()")) #delete

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
        self.created_at = datetime.utcnow()

    def serialize(self):
        return {
            'type': self.type,
            'amount': self.amount,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
        }

#End Models --------------------------------------------------
    
with app.app_context():
    db.create_all()




# Routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))
