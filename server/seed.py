from server.app import db, create_app
from server.extensions import db
from server.models import Restaurant, Pizza, RestaurantPizza

app= create_app()

def seed_data():
    with app.app_context():
        #cllear the existing data
        db.drop_all()
        db.create_all()

        #create the restaurants
        restaurants = [
            Restaurant(name ="Arnolds'_Pizza",address="123 Nairobi"),
            Restaurant(name ="Korirs' Joint", address= "456 Ngong Lane"),
            Restaurant(name="Shell", address="789 Nangiks")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        #Pizzas 
        restaurnt_pizzas = [
            RestaurantPizza(price=20, pizza_id=3, restaurant_id=1),
            RestaurantPizza(price=29, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=8, pizza_id=2, restaurant_id=2),
            RestaurantPizza(price=22, pizza_id=3, restaurant_id=2),
            RestaurantPizza(price=11, pizza_id=1, restaurant_id=3),
            RestaurantPizza(price=18, pizza_id=2, restaurant_id=3),
            
        ]
        db.session.add_all(restaurnt_pizzas)
        db.session.commit()

        print("Database seeded successfully!")

if __name__=='__main__':
    seed_data()


    
