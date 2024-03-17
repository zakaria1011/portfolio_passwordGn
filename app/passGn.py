from flask import render_template, request, Blueprint
import random
import string

dashboard_bp = Blueprint('dashboard', __name__)

def generate_password(length, include_uppercase=True, include_special=True):
    chars = string.ascii_lowercase
    if include_special:
        chars += string.punctuation
    if include_uppercase:
        chars += string.ascii_uppercase
    
    return ''.join(random.choice(chars) for _ in range(length))

@dashboard_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    password = None
    if request.method == 'POST':
        length = int(request.form['length'])
        include_uppercase = 'include_uppercase' in request.form
        include_special = 'include_special' in request.form
        password = generate_password(length, include_uppercase, include_special)
        return render_template('dashboard.html', password=password)
    return render_template('dashboard.html')