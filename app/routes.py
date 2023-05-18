from app import app, db
from app.models import User, Client, Product, Inventory, Purchase, Sale
from flask import render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_login import current_user, login_user, logout_user
import openpyxl
import os
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
    if not(current_user.is_authenticated):
        return redirect(url_for("loginclient"))
    return render_template("sale.html")


@app.route("/init-inventory", methods=["POST"])
def init_inventory():
    products = Product.query.all()
    if len(products) != 0:
        return jsonify({'success':True})
    product1 = Product(1,"Cristal", 0, 0.5, 2.54)
    product2 = Product(2,"Pilsen Callao", 0, 0.5, 2.75)
    product3 = Product(3,"Cusqueña", 0, 0.8, 3.53)
    product4 = Product(4,"Pilsen Trujillo", 0, 0.5, 2.43)
    product5 = Product(5,"Guarana", 0, 0.3, 1.09)
    product6 = Product(6,"Arequipeña", 0, 0.5, 2.62)
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
        return jsonify({'success': True, 'message': f"Product {product_id} updated!"}), 200
    else:
        return jsonify({'success': False, 'message': f"Product {product_id} not found."}), 400


@app.route("/update-inventory-client", methods=["POST"])
def update_inventory_client():
    product_id = request.form.get("productid")
    
    quantity = request.form.get("quantity")
    product = Product.query.get(product_id)
    if product:
        
        # Actualiza los campos del producto con los nuevos valores

        product.stock = product.stock-int(quantity)
        if product.stock <= 0:
            product.stock = 0
        db.session.add(product)

        
# Guarda los cambios en la base de datos

        db.session.commit()
        return jsonify({'success': True, 'message': f"Product {product_id} updated, purchase complete!"})
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
        finally:
            db.session.close()
        return redirect("purchase")
        
            
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
    if not(current_user.is_authenticated):
        return redirect(url_for("login"))

    return render_template("inventory.html")

@app.route("/showinventory", methods=['GET'])
def showinventory():
    try:
        products = Product.query.all()
        products_serialized = [product.serialize() for product in products]
        return jsonify({'success': True, 'products': products_serialized}), 200
    except Exception as e:
        return jsonify({'success': False}), 500

@app.route('/excel', methods=['GET'])
def sendExcel():
    # Realizar la consulta para obtener todos los registros de productos
    productos = Product.query.all()

    # Almacenar los registros de productos en una lista
    lista_productos = []

    for producto in productos:
        # Agregar los campos deseados a la lista de productos
        lista_productos.append({
            'name': producto.name,
            'stock': producto.stock,
            'CVu': producto.CVu,
            'PVu': producto.PVu
        })   
    print(lista_productos)
    ventas = 0
    for producto in lista_productos:
        ventas += producto['PVu'] * producto['stock']
    
    costo_venta = 0
    for producto in lista_productos:
        costo_venta += producto['CVu'] * producto['stock']
    
    
    
    
    # Crear el archivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    
    
    
    # Configurar encabezados
    sheet['A1'] = 'Estado de Resultados'
    sheet['A3'] = 'Ventas'
    sheet['A4'] = 'Costo de ventas'
    sheet['A6'] = 'Margen Bruto'
    sheet['A8'] = 'Gastos Operativos'
    sheet['A9'] = 'Gastos de ventas'
    sheet['A10'] = 'Gastos administrativos'
    sheet['A11'] = 'Otros gastos'
    sheet['A13'] = 'Total de gastos operativos'
    sheet['A15'] = 'Utilidad Operativa'
    sheet['A17'] = 'Otros Ingresos'
    sheet['A18'] = 'Otros Gastos'
    sheet['A20'] = 'Resultado antes de impuestos'
    sheet['A22'] = 'Impuestos'
    sheet['A24'] = 'Utilidad Neta'

    # Ingresar valores
    sheet['B3'] = ventas  # Ventas
    sheet['B4'] = costo_venta  # Costo de ventas

    # Calcular margen bruto
    sheet['B6'] = '=B3-B4'

    # Ingresar valores de gastos operativos
    sheet['B9'] = 0  # Gastos de ventas
    sheet['B10'] = 0  # Gastos administrativos
    sheet['B11'] = 0  # Otros gastos

    # Calcular total de gastos operativos
    sheet['B13'] = '=B9+B10+B11'

    # Calcular utilidad operativa
    sheet['B15'] = '=B6-B13'

    # Ingresar valores de otros ingresos y gastos
    sheet['B17'] = 0  # Otros ingresos
    sheet['B18'] = 0  # Otros gastos

    # Calcular resultado antes de impuestos
    sheet['B20'] = '=B15+B17-B18'

    # Ingresar valor de impuestos
    sheet['B22'] = 1000  # Impuestos

    # Calcular utilidad neta
    sheet['B24'] = '=B20-B22'




    # Guardar el archivo Excel
    nombre_archivo = 'archivo_excel.xlsx'
    ruta = 'app/static/workbooks/'+nombre_archivo
    workbook.save(ruta)

    # Enviar el archivo para su descarga
    return send_file('static\\workbooks\\'+nombre_archivo, as_attachment=True)


@app.route("/logout")
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    logout_user()
    return redirect(url_for("index"))

