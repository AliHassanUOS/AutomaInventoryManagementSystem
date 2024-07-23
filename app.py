from flask import Flask
from config import Config
from models import db
from routes.inventory import inventory_bp
from routes.auth import auth_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(inventory_bp, url_prefix='/inventory')
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def index():
    return 'Welcome to the Automated Inventory Management System!'

if __name__ == '__main__':
    app.run(debug=True)
