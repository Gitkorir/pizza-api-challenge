from server.app import db
from sqlalchemy import CheckConstraint

class RestaurantPizza(db.Model):

    __tablename__='restaurant_pizzas'

    id=db.Column(db.Integer,primary_key =True)
    price=db.Column(db.Integer, nullable=False)
    pizza_id=db.Column(db.Integer, db.ForeignKey('pizza.id'),nullable=False)
    restaurant_id=db.Column(db.Integer,db.ForiegnKey('restaurant.id'), nullable=False)