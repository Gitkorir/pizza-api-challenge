from server.app import db

class Reastaurant(db.Model):
    __tablename__= 'restaurants'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=True,nullable=False)
    address=db.Column(db.String(255), nullable=False)

    #Relationship
    restautant_pizzas = db.relationship('restaurant_pizzas',backref='restaurant',cascade='all,delete-orphan')

    def __repr__(self):
        return f'<Restaurant {self.name}>'
    
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'address':self.address
        }