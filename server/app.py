
from server.config import Config
from flask import Flask
from server.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'  # or your DB URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    #  # Register blueprints (we'll add these later)
    # from server.controllers.restaurant_controller import restaurants_bp
    # from server.controllers.pizza_controller import pizzas_bp
    # from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp
    
    # app.register_blueprint(restaurants_bp)
    # app.register_blueprint(pizzas_bp)
    # app.register_blueprint(restaurant_pizzas_bp)


    return app