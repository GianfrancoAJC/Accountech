from flask import (
    Flask,
    request,
    jsonify,
    abort,
)
from .models import db, setup_db, Employee, Client, Product, Purchase, Sale
from flask_cors import CORS
import http.client
import ssl
import json

def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app, test_config['database_path'] if test_config else None)
        CORS(app, origins=['*'])

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route("/employees", methods=['POST'])
    def register_employee():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if not body['name']:
                list_errors.append('Name is required')
            if not body['email']:
                list_errors.append('Email is required')
            elif not body['email'].endswith('@accountech.com'):
                list_errors.append('Email must end with @accountech.com')
            elif Employee.query.filter_by(email=body['email']).first():
                list_errors.append('Email already exists')
            if not body['password']:
                list_errors.append('Password is required')
            if len(list_errors) == 0:
                name = body['name']
                email = body['email']
                password = body['password']
                employee = Employee(name, email, password)
                db.session.add(employee)
                db.session.commit()
                employee_id = employee.id
        except:
            db.session.rollback()
            returned_code = 500
            abort(returned_code)
        finally:
            db.session.close()
        if len(list_errors) > 0:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), 400
        else:
            return jsonify({
                'success': True,
                'employee_id': employee_id
            }), returned_code

    @app.route("/employee", methods=['GET'])
    def log_employees():
        returned_code = 200
        list_errors = []
        try:
            body = request.json
            if not body['email']:
                list_errors.append('Email is required')
            if not body['password']:
                list_errors.append('Password is required')
            employee = Employee.query.filter_by(email=body['email']).first()
            if not employee:
                list_errors.append('Employee not found')
            elif employee.password != body['password']:
                list_errors.append('Wrong password')
            else:
                employee_id = employee.id
        except:
            returned_code = 500
            abort(returned_code)
        if len(list_errors) > 0:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), 400
        else:
            return jsonify({
                'success': True,
                'employee_id': employee_id
            }), returned_code
        
    @app.route("/clients", methods=['POST'])
    def register_client():
        returned_code = 201
        list_errors = []
        try:
            body = request.json
            if not body['name']:
                list_errors.append('Name is required')
            if not body['email']:
                list_errors.append('Email is required')
            elif Client.query.filter_by(email=body['email']).first():
                list_errors.append('Email already exists')
            conn = http.client.HTTPSConnection("api.eva.pingutil.com", context=ssl._create_unverified_context())
            payload = ''
            headers = {}
            path = "/email?email={}".format(body['email'])
            conn.request("GET", path, payload, headers)
            res = conn.getresponse()
            data = res.read()
            parsed = json.loads(data.decode("utf-8"))
            if parsed["status"] == "failure" or parsed["data"]["deliverable"] == False:
                list_errors.append('Email is not valid')
            if not body['password']:
                list_errors.append('Password is required')
            if len(list_errors) == 0:
                name = body['name']
                email = body['email']
                password = body['password']
                client = Client(name, email, password)
                db.session.add(client)
                db.session.commit()
                client_id = client.id
        except:
            db.session.rollback()
            returned_code = 500
            abort(returned_code)
        finally:
            db.session.close()
        if len(list_errors) > 0:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), 400
        else:
            return jsonify({
                'success': True,
                'client_id': client_id
            }), returned_code
        
    @app.route("/client", methods=['POST'])
    def log_clients():
        returned_code = 200
        list_errors = []
        try:
            body = request.get_json()
            print(body)
            if not body['email']:
                list_errors.append('Email is required')
            if not body['password']:
                list_errors.append('Password is required')
            client = Client.query.filter_by(email=body['email']).first()
            if not client:
                list_errors.append('Client not found')
            elif client.password != body['password']:
                list_errors.append('Wrong password')
            else:
                client_id = client.id
        except:
            returned_code = 500
            abort(returned_code)
        if len(list_errors) > 0:
            return jsonify({
                'success': False,
                'errors': list_errors
            }), 400
        else:
            return jsonify({
                'success': True,
                'client_id': client_id
            }), returned_code

    @app.route("/inventory", methods=["POST"])
    def init_inventory():
        try:
            products = Product.query.all()
            if len(products) != 0:
                return jsonify({'success':True, 'message': 'Inventory already initialized'}), 200
            product1 = Product(1,"Cristal", 0, 0.5, 2.54)
            product2 = Product(2,"Pilsen Callao", 0, 0.5, 2.75)
            product3 = Product(3,"Cusqueña", 0, 0.8, 3.53)
            product4 = Product(4,"Pilsen Trujillo", 0, 0.5, 2.43)
            product5 = Product(5,"Guarana", 0, 0.3, 1.09)
            product6 = Product(6,"Arequipeña", 0, 0.5, 2.62)
            db.session.add_all([product1, product2, product3, product4, product5, product6])
            db.session.commit()
            return jsonify({'success':True, 'message': 'Inventory initialized successfully'}), 200
        except:
            db.session.rollback()
            returned_code = 500
            abort(returned_code)

    @app.route("/inventory", methods=["PATCH"])
    def update_inventory():
        returned_code = 200
        try:
            body = request.json
            product_id = int(body["product_id"])
            quantity = int(body["quantity"])
            product = Product.query.get(product_id)
            if product:
                if body["type"] == "purchase":
                    product.stock = product.stock+quantity
                    employee_id = body["id"]
                    amount = quantity*product.CVu
                    purchase = Purchase(product_id, quantity, amount, employee_id)
                    db.session.add(purchase)
                elif body["type"] == "sale":
                    if product.stock-quantity < 0:
                        product.stock = 0
                        client_id = body["id"]
                        amount = product.stock*product.PVu
                        sale = Sale(product_id, quantity, amount, client_id)
                        db.session.add(sale)
                    else:
                        product.stock = product.stock-quantity
                        client_id = body["id"]
                        amount = quantity*product.PVu
                        sale = Sale(product_id, quantity, amount, client_id)
                        db.session.add(sale)
                db.session.add(product)
                db.session.commit()
            else:
                returned_code = 404
                abort(returned_code)
        except:
            db.session.rollback()
            returned_code = 500
            abort(returned_code)
        finally:
            db.session.close()
        return jsonify({'success':True, 'message': f"Product {product_id} updated"}), returned_code

    @app.route("/inventory", methods=['GET'])
    def showinventory():
        try:
            products = Product.query.all()
            products_serialized = [product.serialize() for product in products]
            if len(products_serialized) == 0:
                return jsonify({'success': False, 'message': 'Inventory is empty'}), 404
            return jsonify({'success': True, 'products': products_serialized}), 200
        except Exception as e:
            returned_code = 500
            abort(returned_code)
    
    @app.route("/inventory>", methods=['DELETE'])
    def deleteproduct():
        try:
            body = request.json
            if body["password"] != "Marvin es el mejor profesor de la UTEC":
                return jsonify({'success': False, 'message': 'Wrong password'}), 400
            if not body["product_id"]:
                return jsonify({'success': False, 'message': 'Product id is required'}), 400
            product_id = body["product_id"]
            product = Product.query.get(product_id)
            if not product:
                return jsonify({'success': False, 'message': 'Product not found'}), 404
            db.session.delete(product)
            db.session.commit()
            return jsonify({'success': True, 'message': f"Product {product_id} deleted"}), 200
        except Exception as e:
            returned_code = 500
            abort(returned_code)
        
    @app.route("/purchase", methods=['GET'])
    def showpurchases():
        try:
            purchases = Purchase.query.all()
            purchases_serialized = [purchase.serialize() for purchase in purchases]
            if len(purchases_serialized) == 0:
                return jsonify({'success': False, 'message': 'No purchases found'}), 404
            return jsonify({'success': True, 'purchases': purchases_serialized}), 200
        except Exception as e:
            returned_code = 500
            abort(returned_code)
        
    @app.route("/sale", methods=['GET'])
    def showsales():
        try:
            sales = Sale.query.all()
            sales_serialized = [sale.serialize() for sale in sales]
            if len(sales_serialized) == 0:
                return jsonify({'success': False, 'message': 'No sales found'}), 404
            return jsonify({'success': True, 'sales': sales_serialized}), 200
        except Exception as e:
            returned_code = 500
            abort(returned_code)

    @app.route('/eerr', methods=['GET'])
    def showeerr():
        try:
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
            ventas = 0
            for producto in lista_productos:
                ventas += producto['PVu'] * producto['stock']
            
            costo_venta = 0
            for producto in lista_productos:
                costo_venta += producto['CVu'] * producto['stock']
            
            utilidad_bruta = ventas - costo_venta
            return jsonify({"1": "Dev. de Ventas\n0",
                            "2": "Ventas\n" + str(ventas),
                            "3": "Ventas brutas\n" + str(ventas),
                            "4": "Costo de ventas\n" + str(costo_venta),
                            "5": "Utilidad bruta\n" + str(utilidad_bruta),
                            "6": "Gastos operativos\n0",
                            "7": "Gasto de ventas\n0",
                            "8": "Otros gastos\n0",
                            "9": "Otros ingresos\n0",
                            "10": "Utilidad operativa\n" + str(utilidad_bruta),
                            "11": "Gastos financieros\n0",
                            "12": "Ingresos financieros\n0",
                            "13": "Utilidad antes de participaciones e impuestos\n" + str(utilidad_bruta),
                            "14": "Participaciones\n0",
                            "15": "Impuestos\n0",
                            "16": "Utilidad neta\n" + str(utilidad_bruta),
                            "success": True}), 200
        except:
            returned_code = 500
            abort(returned_code)

    @app.route('/mcp', methods=['GET']) #margen de contribucion ponderado, sirve para calcular el punto de equilibrio
    def get_pepp():
        try:
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
            stock_total = 0
            for producto in lista_productos:
                stock_total += producto['stock']
            margen = 0
            for producto in lista_productos:
                margen += (producto['PVu'] - producto['CVu']) * producto['stock'] / stock_total
            return jsonify({"mcp": margen, "success": True}), 200
            
        except:
            returned_code = 500
            abort(returned_code)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'message': 'Internal Server error'
        }), 500

    return app


