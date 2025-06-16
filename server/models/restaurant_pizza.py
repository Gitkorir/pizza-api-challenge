from server.app import db
from sqlalchemy import CheckConstraint

class RestaurantPizza(db.Model):

    __tablename__='restaurant_pizzas'

    id=db.Column(db.Integer,primary_key =True)
    price=db.Column(db.Integer, nullable=False)
    pizza_id=db.Column(db.Integer, db.ForeignKey('pizza.id'),nullable=False)
    restaurant_id=db.Column(db.Integer,db.ForiegnKey('restaurant.id'), nullable=False)


    #Price  validation
    __table_args__= (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range')
    )

    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
    
    def to_dict(self):
        return {
            'id':self.id,
            'price':self.price,
            'pizza':self.pizza.to_dict(),
            'restaurant': self.restaurant.to_dict()
        }