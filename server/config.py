import os

class Config:

    SQLAlCHEMY_DATABASE_URI = os.environ.get("sqlite:///pizza_restaurant.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False