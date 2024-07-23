import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    print(SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = 'postgresql://inventory_user:password@localhost/inventory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

