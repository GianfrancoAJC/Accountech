from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    )
from flask_login import (
    LoginManager,
    current_user,
    login_user, 
    logout_user,
    UserMixin
    )
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from datetime import date

app = Flask(__name__)

USER_DB = 'postgres'
PASS_DB = '1234'
URL_DB = 'localhost:5432'
NAME_DB = 'tienda'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'


db              =   SQLAlchemy(app)
migrate         =   Migrate(app, db)
loginManager    =   LoginManager(app)
bcrypt          =   Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return render_template("users.html",
        tittle = "Users", 
        users = User.query.all()
        )

@app.route("/sale")
def sale():
    return render_template("sale.html")

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for("purchase"))

    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
        
            with app.app_context():
                u = User(name, email, password)
                db.session.add(u)
                db.session.commit()

        except:
            flash("Error creating Employee", "danger")

    return render_template("signup.html", tittle = "Signup")


@app.route("/signupclient", methods=["GET", "POST"])
def signupclient():
    
    if current_user.is_authenticated:
        return redirect(url_for("sale"))

    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")

            with app.app_context():
                u = Client(name, email, password)
                db.session.add(u)
                db.session.commit()

        except:
            flash("Error creating Client", "danger")

    return render_template("signupclient.html", tittle = "SignupClient")



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("purchase"))

    if request.method == "POST":
        with app.app_context():
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()

            if user:    
                if user.check_password(password):
                    login_user(user)
                    return redirect(url_for("purchase"))
                else:
                    flash("Wrong password", "danger")

            else:
                flash("User with this email does not exist", "danger")
            
    return render_template("login.html", tittle = "Login")



@app.route('/loginclient', methods=['GET', 'POST'])
def loginclient():
    #Cambiar la redireccion a la interfaz que muestra los inventarios en lugar de index
    if current_user.is_authenticated:
        return redirect(url_for("sale"))


    if request.method == "POST":
        with app.app_context():
            email = request.form.get("email")
            password = request.form.get("password")
            user = Client.query.filter_by(email=email).first()

            if user: 
                if user.check_password(password):
                    login_user(user)
                    return redirect(url_for("sale")) #este "index" hace referencia a la funcion "index" de la linea 7
                else:
                    flash("Wrong password", "danger")

            else:
                flash("User with this email does not exist", "danger")
            
    return render_template("loginclient.html", tittle = "LoginClient")


@app.route("/makepurchase")
def makepurchase():
    #falta agregar la logica para meter las compras
    return render_template("makepurchase.html")


@app.route("/logout")
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    logout_user()
    return redirect(url_for("index"))

@loginManager.user_loader
def load_user(id):
     return User.query.get(int(id))


#Models

#Employee Model
class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35),)
    email = db.Column(db.String(35),nullable=False, unique = True)
    password = db.Column(db.String(64), nullable=False)
    purchases = db.relationship('Purchase', backref='employee', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
         return bcrypt.check_password_hash(self.password, password)


    def __repr__(self):
        return f"Employee {self.id} : {self.name} : {self.email}"
    

#Client Model
class Client(db.Model, UserMixin):
    __tablename__ = "Clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35))
    email = db.Column(db.String(35),nullable=False, unique = True)
    password = db.Column(db.String(64), nullable=False)
    sales = db.relationship('Sale', backref='client', lazy=True)
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    

    def __init__(self, name, email, password,): #Acá falta meter el sales
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"Client {self.id} : {self.name} : {self.email}"


#Product Model
class Product(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    expense = db.Column(db.Integer, nullable=False)
    #imagen = 
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)


    def __init__(self, name, stock, expense): #
        self.name = name
        self.stock = stock
        self.expense = expense

    def __repr__(self):
        return f"Product {self.id} : {self.name} : {self.stock}"



#Product Model
class Inventory(db.Model):
    __tablename__ = "Inventory"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'), nullable=False)


#Purchases
class Purchase(db.Model):
    __tablename__ = "Purchases"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'), nullable=False) #
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)      #
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)


    def __init__(self, product_id, quantity, amount, employee_id):
        self.product_id = product_id
        self.quantity = quantity
        self.amount = amount
        self.employee_id = employee_id

    def __repr__(self):
        return f"Product {self.id} : {self.name} : {self.stock}"


#Sales
class Sale(db.Model):
    __tablename__ = "Sales"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable = False)
    amount = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Clients.id'), nullable=False)
    created_at = db.Column(db.Integer, nullable=False, default=date.today().year)
    modified_at = db.Column(db.Integer, nullable=False, default=date.today().year)

    def __init__(self, product_id, quantity, amount, client_id):
        self.product_id = product_id
        self.quantity = quantity
        self.amount = amount
        self.client_id = client_id

    def __repr__(self):
        return f"Sale {self.id}: Product {self.product_id} - Quantity: {self.quantity} - Amount: {self.amount}"


with app.app_context():
        db.create_all()



if __name__ == "__main__":
    app.run(debug=True)
