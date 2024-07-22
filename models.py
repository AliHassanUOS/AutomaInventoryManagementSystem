from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=False)
