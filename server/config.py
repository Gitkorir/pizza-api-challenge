import os

class Config:

    SQLAlCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or 'sqlite:///pizza_restaurant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False