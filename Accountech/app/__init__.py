#Imports
from flask import (
    Flask, 
    request,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import sys

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/accountech'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Imports

import models
import routes


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))
