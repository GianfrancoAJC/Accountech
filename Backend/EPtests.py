import unittest  # libreria de python para realizar test
from config.qa import config
from app.models import Employee, Department, User
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import io as io
import random
import string


def random_username(char_num):
    return ''.join(random.choice(string.ascii_lowercase)
                   for _ in range(char_num))


class EndPointsTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()

    def test_get_employees(self):
        pass

    def tearDown(self):
        pass
    
