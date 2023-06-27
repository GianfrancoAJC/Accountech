import unittest #libreria de python para realizar test
from config.qa import config 
from app.models import Employee, Department 
from app import create_app 
from flask_sqlalchemy import SQLAlchemy 
import json
import io as io
