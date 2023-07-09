from datetime import date
from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid

db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()

#Employee Model
class Employee(db.Model):
    __tablename__ = "Employees"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(35),)
    email = db.Column(db.String(35),nullable=False, unique = True)
    password = db.Column(db.String(64), nullable=False)
    purchases = db.relationship('Purchase', backref='employee', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Employee {self.name} : {self.email}"
    
    def serialize(self):
        return {
            'id'      : self.id,
            'name'    : self.name,
            'email'   : self.email,
            'password': self.password
        }
    

#Client Model
class Client(db.Model):
    __tablename__ = "Clients"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(35))
    email = db.Column(db.String(35),nullable=False, unique = True)
    password = db.Column(db.String(64), nullable=False)
    sales = db.relationship('Sale', backref='client', lazy=True)
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    

    def __init__(self, name, email, password): #Acá falta meter el sales
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"Client {self.id} : {self.name} : {self.email}"

    def serialize(self):
        return {
            'id'      : self.id,
            'name'    : self.name,
            'email'   : self.email,
            'password': self.password
        }

#Product Model
class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    CVu = db.Column(db.Integer, nullable =False)
    PVu = db.Column(db.Integer, nullable=False) 
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)


    def __init__(self, id, name, stock, CVu, PVu): #
        self.id = id
        self.name = name
        self.stock = stock
        self.CVu = CVu
        self.PVu = PVu

    def __repr__(self):
        return f"Product {self.name} : {self.stock} : {self.PVu}"
    
    def serialize(self):
        return {
            'id'      : self.id,
            'name'    : self.name,
            'stock'   : self.stock,
            'CVu'     : self.CVu,
            'PVu'     : self.PVu
        }

#Purchases
class Purchase(db.Model):
    __tablename__ = "Purchases"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'), nullable=False) #
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.String(120), db.ForeignKey('Employees.id'), nullable=False)      #
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)


    def __init__(self, product_id, quantity, amount, employee_id):
        self.product_id = product_id
        self.quantity = quantity
        self.amount = amount
        self.employee_id = employee_id

    def __repr__(self):
        return f"Product {self.id} : {self.name} : {self.stock}"
    
    def serialize(self):
        return {
            'id'      : self.id,
            'product_id'    : self.product_id,
            'quantity'   : self.quantity,
            'amount'     : self.amount,
            'employee_id'     : self.employee_id
        }


#Sales
class Sale(db.Model):
    __tablename__ = "Sales"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.String(120), db.ForeignKey('Clients.id'), nullable=False)
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)

    def __init__(self, product_id, quantity, amount, client_id):
        self.product_id = product_id
        self.quantity = quantity
        self.amount = amount
        self.client_id = client_id

    def __repr__(self):
        return f"Sale {self.id}: Product {self.product_id} - Quantity: {self.quantity} - Amount: {self.amount}"
    
    def serialize(self):
        return {
            'id'      : self.id,
            'product_id'    : self.product_id,
            'quantity'   : self.quantity,
            'amount'     : self.amount,
            'client_id'     : self.client_id
        }
