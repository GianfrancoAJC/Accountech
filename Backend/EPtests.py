import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import db, Employee, Client, Product, Purchase, Sale
from app import create_app
import json
import random
import string


def random_username(char_num):
    return ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(char_num))


from app.models import db, Employee

class EndPointsTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    #register employees
    def test_register_employee_success(self):
        # Crear un empleado de prueba
        employee_data = {
            'name': 'John Doe',
            'email': 'johndoe@accountech.com',
            'password': 'test123'
        }
        response = self.client.post('/employees', json=employee_data)
        data = json.loads(response.data)

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])

    def test_register_employee_failure(self):
        # Crear un empleado con datos incompletos
        employee_data = {
            'name': 'John Doe',
            'email': '',
            'password': 'test123'
        }
        response = self.client.post('/employees', json=employee_data)
        data = json.loads(response.data)

        # Verificar que la respuesta sea un error 400
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['data'])


    #login employees
    def test_log_employee_success(self):
        # Crear un empleado de prueba en la base de datos
        employee = Employee(name="Test Employee", email="test@accountech.com", password="test123")
        with self.app.app_context():
            db.session.add(employee)
            db.session.commit()

            # Enviar una solicitud POST al endpoint /employee con las credenciales correctas
            employee_data = {
                'email': 'test@accountech.com',
                'password': 'test123'
            }
            response = self.client.post('/employee', json=employee_data)
            data = json.loads(response.data)

            # Verificar que la respuesta sea exitosa
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['data'])
            self.assertEqual(data['data'], employee.id)
    
    def test_log_employee_failure(self):
        # Crear un empleado de prueba en la base de datos
        employee = Employee(name="Test Employee", email="test@accountech.com", password="test123")
        with self.app.app_context():
            db.session.add(employee)
            db.session.commit()

        # Enviar una solicitud POST al endpoint /employee con credenciales incorrectas
        employee_data = {
            'email': 'test@accountech.com',
            'password': 'wrongpassword'  # Contraseña incorrecta
        }
        response = self.client.post('/employee', json=employee_data)
        data = json.loads(response.data)

        # Verificar que la respuesta sea un error 400
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)

           
            
    #show employees
    def test_show_employees(self):
        # Crear un empleado de prueba
        employee = Employee(name="Test Employee", email="test@accountech.com", password="test123")
        with self.app.app_context():
            db.session.add(employee)
            db.session.commit()

        # Realizar una solicitud GET al endpoint /employees
        response = self.client.get("/employees")
        data = json.loads(response.data)

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)

        # Verificar que el empleado de prueba esté en la respuesta
        employees = data["data"]
        self.assertTrue(any(emp["name"] == "Test Employee" for emp in employees))

    def test_show_employees_failure(self):
        # Eliminar todos los empleados de la base de datos
        with self.app.app_context():
            Employee.query.delete()
            db.session.commit()

        # Realizar una solicitud GET al endpoint /employees
        response = self.client.get("/employees")
        data = json.loads(response.data)

        # Verificar que la respuesta sea 404
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["data"], "No employees found")
    