from app import app, db
from app.models import User, Client, Product, Inventory, Purchase, Sale
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user


#routes

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


@app.route("/init-inventory", methods=["POST"])
def init_inventory():
    products = Product.query.all()
    if len(products) != 0:
        return jsonify({'success':True})
    product1 = Product(1,"Cristal", 0, 0, 0.5, 2.54)
    product2 = Product(2,"Pilsen Callao", 0, 0, 0.5, 2.75)
    product3 = Product(3,"Cusqueña", 0, 0, 0.8, 3.53)
    product4 = Product(4,"Pilsen Trujillo", 0, 0, 0.5, 2.43)
    product5 = Product(5,"Guarana", 0, 0, 0.3, 1.09)
    product6 = Product(6,"Arequipeña", 0, 0, 0.5, 2.62)
    db.session.add_all([product1, product2, product3, product4, product5, product6])
    db.session.commit()
    return jsonify({'success':True})


@app.route("/update-inventory", methods=["POST"])
def update_inventory():
    product_id = request.form.get(
"productid"
)
    
    quantity = request.form.get(
"quantity"
)
    product = Product.query.get(product_id)
    if product:
        
# Actualiza los campos del producto con los nuevos valores

        product.stock = product.stock+int(quantity)
        db.session.add(product)

        
# Guarda los cambios en la base de datos

        db.session.commit()
        return jsonify({'success': True, 'message': f"Product {product_id} updated!"})
    else:
        return jsonify({'success': False, 'message': f"Product {product_id} not found."})

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

    return render_template("signup.html")


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
                flash("User you tried to submit does not exist, try again", "danger")
            
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
                flash("User you tried to submit does not exist, try again", "danger")
            
    return render_template("loginclient.html", tittle = "LoginClient")


@app.route("/makepurchase")
def makepurchase():
    return render_template("makepurchase.html")

@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/showinventory", methods=['GET'])
def showinventory():
    try:
        products = Product.query.all()
        products_serialized = [product.serialize() for product in products]
        return jsonify({'success': True, 'products': products_serialized}), 200
    except Exception as e:
        return jsonify({'success': False}), 500

@app.route("/logout")
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    logout_user()
    return redirect(url_for("index"))

