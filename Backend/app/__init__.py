from flask import (
    Flask,
    request,
    jsonify,
    abort,
    render_template,
    redirect,
    url_for,
    flash,
    send_file,
)
from .models import db, setup_db, Employee, Client, Product, Inventory, Purchase, Sale
from flask_cors import CORS
import openpyxl

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
            if not body['password']:
                list_errors.append('Password is required')
            if len(list_errors) == 0:
                name = body['name']
                email = body['email']
                password = body['password']
                employee = Employee(name, email, password)
                employee_id = employee.id
                db.session.add(employee)
                db.session.commit()
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

    @app.route("/employees", methods=['GET'])
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
                'employee': employee_id
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
            if not body['password']:
                list_errors.append('Password is required')
            if len(list_errors) == 0:
                name = body['name']
                email = body['email']
                password = body['password']
                client = Client(name, email, password)
                client_id = client.id
                db.session.add(client)
                db.session.commit()
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
        
    @app.route("/clients", methods=['GET'])
    def log_clients():
        returned_code = 200
        list_errors = []
        try:
            body = request.json
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
                'client': client_id
            }), returned_code

    @app.route("/inventory", methods=["POST"])
    def init_inventory():
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

    @app.route("/inventory", methods=["PATCH"])
    def update_inventory():
        returned_code = 200
        try:
            body = request.json
            product_id = body["productid"]
            quantity = body["quantity"]
            product = Product.query.get(product_id)
            if product:
                if body["type"] == "purchase":
                    product.stock = product.stock+int(quantity)
                elif body["type"] == "sale":
                    if product.stock-int(quantity) < 0:
                        product.stock = 0
                    else:
                        product.stock = product.stock-int(quantity)
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


