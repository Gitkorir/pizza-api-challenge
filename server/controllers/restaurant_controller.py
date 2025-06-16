# server/controllers/restaurant_controller.py
from flask import Blueprint, jsonify, request
from server.models import Restaurant, RestaurantPizza
from server.extensions import db

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    # Get restaurant details with pizzas
    restaurant_data = restaurant.to_dict()
    pizzas = []
    for rp in restaurant.restaurant_pizzas:
        pizza_data = rp.pizza.to_dict()
        pizzas.append(pizza_data)
    
    restaurant_data['pizzas'] = pizzas
    return jsonify(restaurant_data)

@restaurants_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204