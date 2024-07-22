import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://inventory_user:inventory_pass@localhost/inventory_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
