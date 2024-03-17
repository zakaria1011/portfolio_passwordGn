from flask import render_template, Blueprint


index_bp = Blueprint('home', __name__)



@index_bp.route('/')
def index():
    return render_template('index.html')

