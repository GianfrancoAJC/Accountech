from app import app
from flask import render_template

# Routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
