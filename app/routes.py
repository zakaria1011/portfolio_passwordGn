from flask import render_template
from flask import request, jsonify
from flask import redirect, url_for, session
import mysql.connector
import bcrypt
from app import app

db = mysql.connector.connect(
    host="localhost",
    user="passwordgn_dev",
    password="ZaKaria@1011",
    database="passwordgn"
)
cursor = db.cursor()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()
    if user:
        session['user'] = user
        return redirect(url_for('dashboard'))
    else:
        return "Invalid email"
@app.route('/signup', methods=['POST'])

def signup():
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']

    if password != confirm_password:
        return "passwords do not match"

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        return "user already exist"
    cursor.execute("INSERT INTO users (email, password) VALUE %s %s",(email, password))
    db.commit()
    return redirect(url_for('login'))




