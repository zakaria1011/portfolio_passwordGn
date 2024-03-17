from flask import Flask
from passGn import dashboard_bp
from routes import index_bp

app = Flask(__name__)

app.register_blueprint(dashboard_bp)
app.register_blueprint(index_bp)

if __name__ == "__main__":
    app.run(debug=True)